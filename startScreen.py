import pygame,simpleGE
import subprocess,os
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

    def __init__(self):
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

        #Warriors Arena Logo
        self.warriorsArenaLogo = simpleGE.Sprite(self)
        self.warriorsArenaLogo.setImage("startScreen/warriors-arena-logo.png")
        self.warriorsArenaLogo.setSize(80,70)
        self.warriorsArenaLogo.position = (100,240)

        #Cannon Shooter Logo
        self.cannonShooterLogo = simpleGE.Sprite(self)
        self.cannonShooterLogo.setImage("startScreen/cannon-shooter-logo.png")
        self.cannonShooterLogo.setSize(80,70)
        self.cannonShooterLogo.position = (240,240)

        #Charlie Logo
        self.charlieLogo = simpleGE.Sprite(self)
        self.charlieLogo.setImage("startScreen/charlieLogo.png")
        self.charlieLogo.setSize(80,70)
        self.charlieLogo.position = (380,240)

        #Mario Logo
        self.marioLogo = simpleGE.Sprite(self)
        self.marioLogo.setImage("startScreen/marioLogo.png")
        self.marioLogo.setSize(80,70)
        self.marioLogo.position = (521,240)

        #Jump Guy Logo
        self.jumpGuyLogo = simpleGE.Sprite(self)
        self.jumpGuyLogo.setImage("startScreen/jumpGuyLogo.png")
        self.jumpGuyLogo.setSize(80,70)
        self.jumpGuyLogo.position = (100,140)

        #Dice logo
        self.diceLogo = simpleGE.Sprite(self)
        self.diceLogo.setImage("startScreen/diceLogo.png")
        self.diceLogo.setSize(80,70)
        self.diceLogo.position = (240,140)

        #Zombie Land logo
        self.zombieLandLogo = simpleGE.Sprite(self)
        self.zombieLandLogo.setImage("startScreen/zombieLandLogo.png")
        self.zombieLandLogo.setSize(80,70)
        self.zombieLandLogo.position = (380,140)

        #Store Simulator
        self.storeSimLogo = simpleGE.Sprite(self)
        self.storeSimLogo.setImage("startScreen/storeSimulatorLogo.png")
        self.storeSimLogo.setSize(80,70)
        self.storeSimLogo.position = (521,140)

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
        


             

        #Adds all the sprites to the sprite list
        self.sprites = [self.ballState_logo,self.titleLabel,self.selectBorder,self.warriorsArenaLogo,self.playLabel,self.cannonShooterLogo,self.charlieLogo,
                        self.marioLogo,self.jumpGuyLogo,self.diceLogo,self.zombieLandLogo,self.storeSimLogo]

    
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
                
                #Key that plays the game
                if event.key == pygame.K_f:

                    if self.startClicked:
                        pygame.mixer_music.stop()
                        
                        if self.gameSelected == "Warriors-Arena":
                            os.chdir("Warriors-Arena-main")
                            subprocess.call(["python3","userInterface.py"])
                            os.chdir(self.startDir)
                            self.reset()
                        
                        elif self.gameSelected == "Cannon-Shooter":
                            os.chdir("Cannon Shooter")
                            subprocess.call(["python3","CannonDefense.py"])
                            os.chdir(self.startDir)
                            self.reset()

                        elif self.gameSelected == "Charlie-Game":
                            os.chdir("Charlie-Game")
                            subprocess.call(["python3","catch8.py"])
                            os.chdir(self.startDir)
                            self.reset()
                        
                        elif self.gameSelected == "Mario-Game":
                            os.chdir("Janitoring_Game-main")
                            subprocess.call(["python3","JanitorGame.Complete.py"])
                            os.chdir(self.startDir)
                            self.reset()
                        
                        elif self.gameSelected == "JumpGuy-Game":
                            os.chdir("jumpGuy-main")
                            subprocess.call(["python3","main.py"])
                            os.chdir(self.startDir)
                            self.reset()
                        
                        elif self.gameSelected == "Dice-Game":
                            os.chdir("FinalDice-main")
                            subprocess.call(["python3","barDice.py"])
                            os.chdir(self.startDir)
                            self.reset()
                        
                        elif self.gameSelected == "ZombieLand-Game":
                            os.chdir("Zombie-Land-Game-main")
                            subprocess.call(["python3","ZombieLand.py"])
                            os.chdir(self.startDir)
                            self.reset()
                        
                        elif self.gameSelected == "StoreSim-Game":
                            os.chdir("Store-Simulator-Final-main")
                            subprocess.call(["python3","carterLeckron_finalProject_storeSimulator.py"])
                            os.chdir(self.startDir)
                            self.reset()

                


    #This is going to look for keyboard input(Joystick mapping) and decide what the selection is
    def process(self): 

        #First Row
        if self.x == 1 and self.y == 0:
            self.selectBorder.show()
            self.selectBorder.position = self.warriorsArenaLogo.position
            self.playLabel.show()
            self.gameSelected = "Warriors-Arena"
            self.startClicked = True
        
        if self.x == 2 and self.y == 0:
            self.selectBorder.position = self.cannonShooterLogo.position
            self.gameSelected = "Cannon-Shooter"
            self.startClicked = True

        if self.x == 3 and self.y == 0:
            self.selectBorder.position = self.charlieLogo.position
            self.gameSelected = "Charlie-Game"
            self.startClicked = True
        
        if self.x == 4 and self.y == 0:
            self.selectBorder.position = self.marioLogo.position
            self.gameSelected = "Mario-Game"
            self.startClicked = True
        
        #Second row
        if self.x == 1 and self.y == 1:
            self.selectBorder.position = self.jumpGuyLogo.position
            self.gameSelected = "JumpGuy-Game"
            self.startClicked = True

        if self.x == 2 and self.y == 1:
            self.selectBorder.position = self.diceLogo.position
            self.gameSelected = "Dice-Game"
            self.startClicked = True
        
        if self.x == 3 and self.y == 1:
            self.selectBorder.position = self.zombieLandLogo.position
            self.gameSelected = "ZombieLand-Game"
            self.startClicked = True
        
        if self.x == 4 and self.y == 1:
            self.selectBorder.position = self.storeSimLogo.position
            self.gameSelected = "StoreSim-Game"
            self.startClicked = True

    

        #Sets x to zero if it goes off of the screen and hides the sprite or if its greater then 3 it sets it back to 3
        if self.x <= 0 and not(self.startClicked):
            self.x = 0
        
        if self.x <= 0 and self.startClicked:
            self.x = 4
        
        if self.x > 4:
            self.x = 1

        if self.y < 0:
            self.y = 0
        
        if self.y > 1:
            self.y = 1
        

        #Exits the games if all of the left buttons are being held at the same time(Inteded to help get out of full screen)
        if self.isKeyPressed(pygame.K_f) and self.isKeyPressed(pygame.K_e) and self.isKeyPressed(pygame.K_z) and self.isKeyPressed(pygame.K_x) and self.isKeyPressed(pygame.K_q):
            self.stop()
            







#Main function that starts the scene
def main():

    #Initializes start screen and keepGoing for while loop
    startScreen = StartScreen()
    startScreen.start()


if __name__ == "__main__":
    main()