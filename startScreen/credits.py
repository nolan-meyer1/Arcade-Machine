import simpleGE,pygame
"""
This file contains the credits. This will have everyone's name for 
who made what game. Is activated on the machine by clicking one of 
the side buttons. 

Nolan Meyer

April 8th, 2024
"""

#Credits scene
class Credits(simpleGE.Scene):

    def __init__(self):
        super().__init__()

        #Creates the background image and sets the caption of the screen
        self.setCaption("Credits")
        self.background = pygame.image.load("arcadeBackground.jpg")
        self.background = self.background.convert_alpha()
        self.background = pygame.transform.scale(self.background,self.screen.get_size())

        #Creates the title image
        self.titleLabel = simpleGE.Label()
        self.titleLabel.text = "CS 120 Games!"
        self.titleLabel.center = (320,230)
        self.titleLabel.clearBack = True
        self.titleLabel.size = (400,400)
        self.titleLabel.font = pygame.font.Font("ARCADE_N.TTF",30)
        self.titleLabel.fgColor = (255,215,0)

        #Image logos
        self.warriorsArenaLogo = simpleGE.Sprite(self)
        self.warriorsArenaLogo.setImage("warriors-arena-logo.png")
        self.warriorsArenaLogo.setSize(80,70)
        self.warriorsArenaLogo.position = (50,130)

        self.cannonShooterLogo = simpleGE.Sprite(self)
        self.cannonShooterLogo.setImage("cannon-shooter-logo.png")
        self.cannonShooterLogo.setSize(80,70)
        self.cannonShooterLogo.position = (50,220)

        self.charlieLogo = simpleGE.Sprite(self)
        self.charlieLogo.setImage("charlieLogo.png")
        self.charlieLogo.setSize(80,70)
        self.charlieLogo.position = (50,310)

        self.marioLogo = simpleGE.Sprite(self)
        self.marioLogo.setImage("marioLogo.png")
        self.marioLogo.setSize(80,70)
        self.marioLogo.position = (50,400)

        #Credit Labels
        self.warriorsLabel = simpleGE.Label()
        self.warriorsLabel.text = "Warriors Arena- Nolan Meyer"
        self.warriorsLabel.center = (250,140)
        self.warriorsLabel.clearBack = True
        self.warriorsLabel.size = (300,50)
        self.warriorsLabel.fgColor = (255,215,0)

        self.cannonLabel = simpleGE.Label()
        self.cannonLabel.text = "Cannon Shooter- Karter West"
        self.cannonLabel.center = (250,230)
        self.cannonLabel.clearBack = True
        self.cannonLabel.size = (300,50)
        self.cannonLabel.fgColor = (255,215,0)

        self.charlieLabel = simpleGE.Label()
        self.charlieLabel.text = "Charlie- Proffesor Andy Harris"
        self.charlieLabel.center = (250,320)
        self.charlieLabel.clearBack = True
        self.charlieLabel.size = (300,50)
        self.charlieLabel.fgColor = (255,215,0)

        self.marioLabel = simpleGE.Label()
        self.marioLabel.text = "Janitor Game- Lance Schoenradt"
        self.marioLabel.center = (260,410)
        self.marioLabel.clearBack = True
        self.marioLabel.size = (325,50)
        self.marioLabel.fgColor = (255,215,0)


        #Keeps track of what page we're on and keeps track if you want to quit
        self.pageNumber = 0
        self.action = ""




        self.sprites = [self.titleLabel,self.warriorsArenaLogo,self.warriorsLabel,self.cannonShooterLogo,self.cannonLabel
                        ,self.charlieLogo,self.charlieLabel,self.marioLogo,self.marioLabel]
        
    
    #Overrides process method that will look at what page it's on and if you want to exit
    def processEvent(self, event):
        
        #Checks for key input
        if event.type == pygame.KEYDOWN:

            #Track joystick 

            if event.key == pygame.K_d:
                self.action = "Page2"
                self.stop()

            #Exits the page
            if event.key == pygame.K_SLASH:
                self.action = "Quit"
                self.stop()

            

#Class for second page 
class Credits2(Credits):

    def __init__(self):
        super().__init__()

        #Creates the background image and sets the caption of the screen
        self.setCaption("Credits")
        self.background = pygame.image.load("arcadeBackground.jpg")
        self.background = self.background.convert_alpha()
        self.background = pygame.transform.scale(self.background,self.screen.get_size())

        #Creates the title image
        self.titleLabel = simpleGE.Label()
        self.titleLabel.text = "CS 120 Games!"
        self.titleLabel.center = (320,230)
        self.titleLabel.clearBack = True
        self.titleLabel.size = (400,400)
        self.titleLabel.font = pygame.font.Font("ARCADE_N.TTF",30)
        self.titleLabel.fgColor = (255,215,0)

        #Image logos
        self.jumpGuyLogo = simpleGE.Sprite(self)
        self.jumpGuyLogo.setImage("jumpGuyLogo.png")
        self.jumpGuyLogo.setSize(80,70)
        self.jumpGuyLogo.position = (50,130)

        self.zombieLandLogo = simpleGE.Sprite(self)
        self.zombieLandLogo.setImage("zombieLandLogo.png")
        self.zombieLandLogo.setSize(80,70)
        self.zombieLandLogo.position = (50,220)

        self.storeLogo = simpleGE.Sprite(self)
        self.storeLogo.setImage("storeSimulatorLogo.png")
        self.storeLogo.setSize(80,70)
        self.storeLogo.position = (50,310)

        #Credit Labels
        self.jumpGuyLabel = simpleGE.Label()
        self.jumpGuyLabel.text = "Jump Guy- Unknown"
        self.jumpGuyLabel.center = (210,140)
        self.jumpGuyLabel.clearBack = True
        self.jumpGuyLabel.size = (300,50)
        self.jumpGuyLabel.fgColor = (255,215,0)

        self.zombieLabel = simpleGE.Label()
        self.zombieLabel.text = "Zombie Land- Unknown"
        self.zombieLabel.center = (210,230)
        self.zombieLabel.clearBack = True
        self.zombieLabel.size = (300,50)
        self.zombieLabel.fgColor = (255,215,0)

        self.storeLabel = simpleGE.Label()
        self.storeLabel.text = "Store Simulator- Carter Lekron"
        self.storeLabel.center = (250,320)
        self.storeLabel.clearBack = True
        self.storeLabel.size = (320,50)
        self.storeLabel.fgColor = (255,215,0)

        self.sprites = [self.titleLabel,self.jumpGuyLogo,self.zombieLandLogo,self.storeLogo,self.storeLabel,self.jumpGuyLabel,self.zombieLabel]
        
        
    #Overrides process method that will look at what page it's on and if you want to exit
    def processEvent(self, event):
        
        #Checks for key input
        if event.type == pygame.KEYDOWN:
        
            #Track joystick 
            if event.key == pygame.K_a:
                self.stop()
            
            #Exits the page
            if event.key == pygame.K_SLASH:
                self.action = "Quit"
                self.stop()
            
    




def main():
    keepGoing = True

    while keepGoing:
            
            page1 = Credits()
            page1.start()
            
            if page1.action == "Page2":
                page2 = Credits2()
                page2.start()

            
            if page1.action == "Quit" or page2.action == "Quit":
                keepGoing = False


if __name__ == "__main__":
    main()