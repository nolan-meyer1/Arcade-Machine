import pygame,simpleGE
import subprocess,os,json
"""
This file contains the start 
screen for an Arcade machine located
at Ball State in the Computer Science Department. 
All image citations below. 

Ball State Logo: Taken from official twitter page
Arcade Background Image: https://www.vecteezy.com/vector-art/5266448-vector-retro-futuristic-background
Arcade Font: https://www.dafont.com/arcade-ya.font
Selection Border: https://pngimg.com/image/90845
Arcade Music: Music by <a href="https://pixabay.com/users/grand_project-19033897/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=128379">Grand_Project</a> from <a href="https://pixabay.com/music//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=128379">Pixabay</a>

Nolan Meyer

March 21, 2023
"""

#Creates the class that contains the scene
class StartScreen(simpleGE.Scene):

    def __init__(self,configurationFile):
        super().__init__()
        
        #Creates the background image and sets the caption of the screen
        self.setCaption("Arcade Machine")
        self.background = pygame.image.load("startScreen/arcadeBackground.jpg")
        self.background = self.background.convert_alpha()
        self.background = pygame.transform.scale(self.background,self.screen.get_size())

        #Adds the image for the ball state logo in the corner
        self.ballState_logo = simpleGE.Sprite(self)
        self.ballState_logo.setImage("startScreen/ballStateLogo.jpg")
        self.ballState_logo.setSize(80,80)
        self.ballState_logo.position = (600,445)

        #Creates the title image
        self.titleLabel = simpleGE.Label()
        self.titleLabel.text = "CS 120 Games!"
        self.titleLabel.center = (320,230)
        self.titleLabel.clearBack = True
        self.titleLabel.size = (400,400)
        self.titleLabel.font = pygame.font.Font("startScreen/ARCADE_N.TTF",30)
        self.titleLabel.fgColor = (255,215,0)

        #Creates the pop up that tells what button to click when ready to play
        self.playLabel = simpleGE.Label()
        self.playLabel.text = "Click Red to Play!"
        self.playLabel.center = (320,550)
        self.playLabel.clearBack = True
        self.playLabel.size = (520,400)
        self.playLabel.font = pygame.font.Font("startScreen/ARCADE_N.TTF",30)
        self.playLabel.fgColor = (255,215,0)
        self.playLabel.hide()

        #Border that shows that something is selected
        self.selectBorder = simpleGE.Sprite(self)
        self.selectBorder.setImage("startScreen/selectionBorder.png")
        self.selectBorder.setSize(120,120)
        self.selectBorder.position = (120,120)
        self.selectBorder.hide()

        #Game images
        self.game1 = simpleGE.Sprite(self)
        self.game2 = simpleGE.Sprite(self)
        self.game3 = simpleGE.Sprite(self)
        self.game4 = simpleGE.Sprite(self)
        self.game5 = simpleGE.Sprite(self)
        self.game6 = simpleGE.Sprite(self)
        self.game7 = simpleGE.Sprite(self)
        self.game8 = simpleGE.Sprite(self)
        
        #Credits Label
        self.creditsLabel = simpleGE.Label()
        self.creditsLabel.text = "Left Side Button: Credits"
        self.creditsLabel.center = (140,470)
        self.creditsLabel.clearBack = True
        self.creditsLabel.size = (300,50)
        self.creditsLabel.fgColor = (255,215,0)

        #Grabs the current working directory that we're in when the game first runs and stors it in a variable so we can
        #always get back to the starting position
        self.startDir = os.getcwd()


        #Initializes Arcade Music
        pygame.mixer.music.load("startScreen/arcadeMusic.mp3")
        pygame.mixer.music.set_volume(.3)
        pygame.mixer.music.play(-1)

        #Keeps track if a current game is selected or not
        self.gameSelected = ""
        self.startClicked = False
        self.x = 0
        self.y = 0

        #Keeps track of the number of games. This is used for limits to control where the selection border goes
        self.numberOfGamesX = 0
        self.numberOfGamesY = 0

        #Contains the configuration file
        self.configurationFile = configurationFile

        #Contains a list of all the games and sets all of the states to be originally blank
        self.gameList = [self.game1,self.game2,self.game3,self.game4,self.game5,self.game6,self.game7,self.game8]

        for game in self.gameList:
            game.hide()
    

        #Adds all the sprites to the sprite list
        self.sprites = [self.ballState_logo,self.titleLabel,self.selectBorder,self.gameList,self.playLabel,self.creditsLabel]

    
    #Resets everything on the screen
    def reset(self):
        self.gameSelected = ""
        self.selectBorder.hide()
        self.playLabel.hide()
        self.startClicked = False
        self.x = 0
        self.y = 0
        pygame.mixer.music.play(-1)

    
    #Checks for Key Down
    def processEvent(self, event):

            #Checks if the key is down and adds one
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_d:
                    self.x += 1

                if event.key == pygame.K_a:
                    self.x -= 1

                if event.key == pygame.K_w:
                    self.y += 1
                
                if event.key == pygame.K_s:
                    self.y -= 1

                if event.key == pygame.K_SLASH:
                    self.runGame("startScreen","credits.py")

                 
                
                #Key that plays the game
                if event.key == pygame.K_f:

                    if self.startClicked:
                        pygame.mixer_music.stop()

                        #First Row
                        if self.x == 1 and self.y == 0:
                            self.runGame(self.configurationFile["Games"][0]["dir"],self.configurationFile["Games"][0]["startFile"])
                        
                        if self.x == 2 and self.y == 0:
                            self.runGame(self.configurationFile["Games"][1]["dir"],self.configurationFile["Games"][1]["startFile"])

                        if self.x == 3 and self.y == 0:
                            self.runGame(self.configurationFile["Games"][2]["dir"],self.configurationFile["Games"][2]["startFile"])
                        
                        if self.x == 4 and self.y == 0:
                            self.runGame(self.configurationFile["Games"][3]["dir"],self.configurationFile["Games"][3]["startFile"])
                        
                        #Second row
                        if self.x == 1 and self.y == 1:
                            self.runGame(self.configurationFile["Games"][4]["dir"],self.configurationFile["Games"][4]["startFile"])

                        if self.x == 2 and self.y == 1:
                            self.runGame(self.configurationFile["Games"][5]["dir"],self.configurationFile["Games"][5]["startFile"])
                        
                        if self.x == 3 and self.y == 1:
                            self.runGame(self.configurationFile["Games"][6]["dir"],self.configurationFile["Games"][6]["startFile"])
                        
                        if self.x == 4 and self.y == 1:
                            self.runGame(self.configurationFile["Games"][7]["dir"],self.configurationFile["Games"][7]["startFile"])
                        


    #This is going to look for keyboard input(Joystick mapping) and decide what the selection is
    def process(self): 

        #First Row
        if self.x == 1 and self.y == 0:
            self.selectBorder.show()
            self.selectBorder.position = self.game1.position
            self.playLabel.show()
            self.startClicked = True
        
        if self.x == 2 and self.y == 0:
            if self.game2.visible:
                self.selectBorder.position = self.game2.position
                self.startClicked = True
            else:
                self.x = 1

        if self.x == 3 and self.y == 0:
            if self.game3.visible:
                self.selectBorder.position = self.game3.position
                self.startClicked = True
            else:
                self.x = 1
        
        if self.x == 4 and self.y == 0:
            if self.game4.visible:
                self.selectBorder.position = self.game4.position
                self.startClicked = True
            else:
                self.x = 1
            
        
        #Second row
        if self.x == 1 and self.y == 1:
            if self.game5.visible:
                self.selectBorder.position = self.game5.position
                self.startClicked = True
            else:
                self.x = 1

        if self.x == 2 and self.y == 1:
            if self.game6.visible:
                self.selectBorder.position = self.game6.position
                self.startClicked = True
            else:
                self.x = 1
        
        if self.x == 3 and self.y == 1:
            if self.game7.visible:
                self.selectBorder.position = self.game7.position
                self.startClicked = True
            else:
                self.x = 1
        
        if self.x == 4 and self.y == 1:
            if self.game8.visible:
                self.selectBorder.position = self.game8.position
                self.startClicked = True
            else:
                self.x = 1

    
        #Sets x to zero if it goes off of the screen and hides the sprite or if its greater then 3 it sets it back to 3
        if self.x <= 0 and not(self.startClicked):
            self.x = 0
        
        if self.x <= 0 and self.startClicked:
            self.x = 4
        
        if self.x > self.numberOfGamesX:
            self.x = 1

        if self.y < 0:
            self.y = 0
        
        if self.y > self.numberOfGamesY:
            self.y = self.numberOfGamesY
        

        #Exits the games if all of the left buttons are being held at the same time(Inteded to help get out of full screen)
        if self.isKeyPressed(pygame.K_f) and self.isKeyPressed(pygame.K_e) and self.isKeyPressed(pygame.K_z) and self.isKeyPressed(pygame.K_x) and self.isKeyPressed(pygame.K_q):
            self.stop()
    
    #Runs the game 
    def runGame(self,gameDir,gameFile):
        os.chdir(gameDir)
        subprocess.call(["python3",gameFile])
        os.chdir(self.startDir)

        if gameFile != "credits.py":
            self.reset()


#Creates the screen
def loadPage():

    i = 0
    j = 0

    with open("configuration.json","r") as file:
        games = json.load(file)
    
    page = StartScreen(configurationFile=games)

    

    for game in games["Games"]:

        
        if i < 4:
            gameEdited = page.gameList[i]

            gameEdited.setImage(game["Image-Path"])
            gameEdited.setSize(80,70)
            gameEdited.show()
            gameEdited.position = (100 + (i * 140),240)
            

            i += 1

            page.numberOfGamesX += 1
        
        elif i >= 4:

            gameEdited = page.gameList[i]

            gameEdited.setImage(game["Image-Path"])
            gameEdited.setSize(80,70)
            gameEdited.show()
            gameEdited.position = (100 + (j * 140),140)
                
            i += 1
            j += 1 
    
    #Checks if there are more than 4 games. If there is add to number of games which adds to the Y boundary for selection border
    if len(games["Games"]) > 4:
        page.numberOfGamesY += 1

    
    return page

        


#Main function that starts the scene
def main():

    #Initializes start screen and keepGoing for while loop
    #startScreen = StartScreen()
    #startScreen.start()

    gamePages = loadPage()
    gamePages.start()


if __name__ == "__main__":
    main()