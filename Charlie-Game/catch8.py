import pygame, random, simpleGE

""" catch the Cash 8
    Instructions and state
"""

class Coin(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Coin.png")
        self.setSize(25, 25)
        self.reset()
        
    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint((pygame.display.get_window_size()[1] // 480) * 3, (pygame.display.get_window_size()[1] // 480) * 8)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()

class Charlie(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Charlie.png")
        self.setSize(50, 50)
        self.position = (320, 400)
        self.moveSpeed = pygame.display.get_window_size()[0] // 640 * 5
    
    def process(self):
        if self.isKeyPressed(pygame.K_a):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_d):
            self.x += self.moveSpeed     
            
class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (100, 30)
        
class LblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time Left: 10"
        self.center = (500, 30)

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("Campus.jpg")
        
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 10
        self.score = 0
        
        self.sndCoin = simpleGE.Sound("coin.wav")
        
        self.charlie = Charlie(self)
        self.coins = []
        for i in range(10):
            self.coins.append(Coin(self))
            
        self.lblScore = LblScore()
        self.lblTime = LblTime()
        
        self.sprites = [self.charlie,
                        self.coins,
                        self.lblScore, 
                        self.lblTime]
    def resize(self):
        """
        Defualt window size is 640 by 480. This function 
        makes a ratio based off that size and updates 
        everything on the screen to be rezised with whatever
        the current size of the full screen is. 
        """

        windowSize = pygame.display.get_window_size()

        #Used for scailing
        ratioX = windowSize[0] / 640
        ratioY = windowSize[1] / 480

        #Updates charlie
        self.charlie.setSize(ratioX * 50,ratioY * 50)
        self.charlie.position = (ratioX * self.charlie.x,ratioY * self.charlie.y)

        #Updates coin size
        for coin in self.coins:
            coin.setSize(ratioX * 25,ratioY * 25)
        
        #Updates the labels positions
        self.lblScore.center = (ratioX * 100,ratioY * 30)
        self.lblTime.center = (ratioX * 500,ratioY * 30)
        
    def process(self):
        for coin in self.coins:
            if self.charlie.collidesWith(coin):
                self.sndCoin.play()
                coin.reset()
                self.score += 1
                self.lblScore.text = f"Score: {self.score}"
                
        self.lblTime.text = f"Time Left: {self.timer.getTimeLeft():.2f}"
        if self.timer.getTimeLeft() < 0:
            print(f"Final Score: {self.score}")
            self.stop()

class Instructions(simpleGE.Scene):
    def __init__(self, score):
        super().__init__()
        self.setImage("campus.jpg")
        
        self.response = "Play"
        
        self.instructions = simpleGE.MultiLabel()
        self.instructions.textLines = [
        "You are Charlie the Cardinal.",
        "Move with the left and right arrow keys",
        "and catch as much cash as you can",
        "in only ten seconds",
        "",
        "Good Luck!"]
        
        self.instructions.center = (320, 240)
        self.instructions.size = (500, 250)
        
        self.prevScore = score
        self.lblScore = simpleGE.Label()
        self.lblScore.text = f"Last score: {self.prevScore}"
        self.lblScore.center = (320, 400)
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Play (up)"
        self.btnPlay.center = (100, 400)
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit (down)"
        self.btnQuit.center = (550, 400)
        
        self.sprites = [self.instructions,
                        self.lblScore,
                        self.btnQuit,
                        self.btnPlay]
    
    def resize(self):
        """
        Resizes elements to scale up to full screen
        """

        windowSize = pygame.display.get_window_size()

        #Used for scailing
        ratioX = windowSize[0] / 640
        ratioY = windowSize[1] / 480

        #Updates main instructions label
        self.instructions.center = (ratioX * 320,ratioY * 240)

        #Updates the buttons
        self.btnPlay.center = (ratioX * 100,ratioY * 400)
        self.btnQuit.center = (ratioX * 550,ratioY * 400)

        #Last score label
        self.lblScore.center = (ratioX * 320,ratioY * 400)
        
    def process(self):
        #buttons
        if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop()
        if self.btnPlay.clicked:
            self.response = "Play"
            self.stop()

        #arrow keys
        if self.isKeyPressed(pygame.K_w):
            self.response = "Play"
            self.stop()
        if self.isKeyPressed(pygame.K_s):
            self.response = "Quit"
            self.stop()

def main():
    
    keepGoing = True
    score = 0
    while keepGoing:
        
        instructions = Instructions(score)
        instructions.resize()
        instructions.start()
                
        if instructions.response == "Play":    
            game = Game()
            game.resize()
            game.start()
            score = game.score
        else:
            keepGoing = False
    
if __name__ == "__main__":
    main()
