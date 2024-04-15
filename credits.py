import simpleGE,pygame,json
"""
This file contains the credits. This will have everyone's name for 
who made what game. Is activated on the machine by clicking one of 
the side buttons. 

Nolan Meyer

April 8th, 2024
"""

#Credits scene
class Credits(simpleGE.Scene):

    currentPage = 1
    numberPages = 0
    creditsPages = ""

    def __init__(self):
        super().__init__()

        #Incriments the number of pages
        Credits.numberPages += 1
        self.pageNum = Credits.numberPages

        #Creates the background image and sets the caption of the screen
        self.setCaption("Credits")
        self.background = pygame.image.load("startScreen/arcadeBackground.jpg")
        self.background = self.background.convert_alpha()
        self.background = pygame.transform.scale(self.background,self.screen.get_size())

        #Creates the title image
        self.titleLabel = simpleGE.Label()
        self.titleLabel.text = "CS 120 Games!"
        self.titleLabel.center = (320,230)
        self.titleLabel.clearBack = True
        self.titleLabel.size = (400,400)
        self.titleLabel.font = pygame.font.Font("startScreen/ARCADE_N.TTF",30)
        self.titleLabel.fgColor = (255,215,0)

        #Image logos
        self.gameLogo1 = simpleGE.Sprite(self)
        self.gameLogo2 = simpleGE.Sprite(self)
        self.gameLogo3 = simpleGE.Sprite(self)
        self.gameLogo4 = simpleGE.Sprite(self)

        #Credit Labels
        self.gameLabel1 = simpleGE.Label()
        self.gameLabel2 = simpleGE.Label()
        self.gameLabel3 = simpleGE.Label()
        self.gameLabel4 = simpleGE.Label()
    


        #Keeps track of what page we're on and keeps track if you want to quit
        self.pageNumber = 0
        self.action = ""

        #Keeps track of all the images/labels
        self.logoList = [self.gameLogo1,self.gameLogo2,self.gameLogo3,self.gameLogo4]
        self.labelList = [self.gameLabel1,self.gameLabel2,self.gameLabel3,self.gameLabel4]

        #Sets everything to hidden
        for logo in self.logoList:
            logo.hide()
        
        for label in self.labelList:
            label.hide()

        self.sprites = [self.titleLabel,self.logoList,self.labelList]
        
    
    #Overrides process method that will look at what page it's on and if you want to exit
    def processEvent(self, event):
        """
        Keeps track of key board input. Incriments and decreaes current page
        based off what page you want to go to. 
        """
        
        #Checks for key input
        if event.type == pygame.KEYDOWN:

            #Track joystick 

            if event.key == pygame.K_d:
                if (Credits.numberPages) > 0 and ((Credits.currentPage + 1) <= Credits.numberPages):
                    Credits.currentPage += 1
            
            if event.key == pygame.K_a:
                if (Credits.numberPages) > 0 and ((Credits.currentPage - 1) > 0):
                    Credits.currentPage -= 1

            #Exits the page
            if event.key == pygame.K_SLASH:
                self.action = "Quit"
                self.stop()
    
    #Keeps track of what page we're going to
    def process(self):
        """
        This will make the scene transition
        if the current page does not equal
        the current page. 
        """

        if Credits.currentPage != self.pageNum:
            self.stop()
            Credits.creditsPages[Credits.currentPage].start()


    
#Creates how ever many pages that you need
def loadPage(games,pages=[None]):
    """
    Takes in a dictionary loaded in from 
    a configuration file. Loops over that entire dictionary. 
    If there are more than 8 on the screen it will make a recursive
    call passing in a sliced list containing the remaning left.
    """

    i = 0

    initialLength = len(games["Games"])

    page = Credits()

    for game in games["Games"]:

        
        if i < 4:

            #Sets the game
            logoEdited = page.logoList[i]
            labelEdited = page.labelList[i]

            logoEdited.setImage(game["Image-Path"])
            logoEdited.setSize(80,70)
            logoEdited.show()
            logoEdited.position = (50,130 + (i * 90))

            labelEdited.text = game["Name"]
            labelEdited.center = (300,140 + (i * 90))
            labelEdited.clearBack = True
            labelEdited.size = (400,50)
            labelEdited.fgColor = (255,215,0)
            

            i += 1
        
        else:
            break
        
    
    #Adds to the pagesList
    pages.append(page)


    #Resursive Call/Base Case
    if len(games["Games"]) > 4:

        tempGame = games.copy()
        tempGame["Games"] = tempGame["Games"][i:]

        pages = loadPage(tempGame,pages)
        
    
    return pages
            
    



def main():
    
    #Loads the file in that we need
    with open("configuration.json","r") as file:
        games = json.load(file)
    
    gamePages = loadPage(games)
    Credits.creditsPages = gamePages

    gamePages[Credits.currentPage].start()


if __name__ == "__main__":
    main()