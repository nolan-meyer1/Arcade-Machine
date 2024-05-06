import pygame, simpleGE, random

class Spaceship(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Spaceship_rotated.png")
        self.setSize(30, 30)
        
    def process(self):
        if self.isKeyPressed(pygame.K_a):
            self.imageAngle += 6
        if self.isKeyPressed(pygame.K_d):
            self.imageAngle -= 6
        if self.isKeyPressed(pygame.K_w):
            self.addForce(.2, self.imageAngle)
        if self.isKeyPressed(pygame.K_s):
            self.addForce(-.2, self.imageAngle)

class Asteroid(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Asteroid.png")
        self.setSize(35, 35)
        self.minSpeed = 2
        self.maxSpeed = 4
        self.reset()
        
    def reset(self):
        self.y = random.randint(0, self.screenHeight)
        self.x = random.randint(0, self.screenWidth)
        self.dx = random.randint(self.minSpeed, self.maxSpeed)
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
        
    def CheckBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
        if self.top < self.screenHeight:
            self.reset()
        if self.right > self.screenWidth:
            self.reset()
        if self.left < self.screenWidth:
            self.reset()

class DarkMatter(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("DM_Potion.png")
        self.setSize(35, 35)
        self.minSpeed = 1
        self.maxSpeed = 4
        self.reset()
        
    def reset(self):
        self.y = random.randint(0, self.screenHeight)
        self.x = random.randint(0, self.screenWidth)
        self.dx = random.randint(self.minSpeed, self.maxSpeed)
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
        
    def CheckBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
        if self.top < self.screenHeight:
            self.reset()
        if self.right > self.screenWidth:
            self.reset()
        if self.left < self.screenWidth:
            self.reset()
            
class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (100, 30)
        
class Bullet(simpleGE.Sprite):
    def __init__(self, scene, parent):
        super().__init__(scene)
        self.parent = parent
        self.colorRect("White", (5,5))
        self.setBoundAction(self.HIDE)
        self.hide()
        
    def fire(self):
        if not self.visible:
            self.show()
            self.position = self.parent.position
            self.moveAngle = self.parent.imageAngle
            self.speed = 50
            
    
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("OrionNebula.jpg")
        self.spaceship = Spaceship(self)
        self.bullet = Bullet(self, self.spaceship)
        self.deathflash = simpleGE.Sound("DeathFlash.flac")
        self.numAsteroids = 4
        self.score = 0
        
        self.lblScore = LblScore()
        
        self.asteroids = []
        for i in range(self.numAsteroids):
            self.asteroids.append(Asteroid(self))
        
        self.darkmatter = DarkMatter(self)
        self.collect = simpleGE.Sound("sfx_pick.flac")
        self.sprites = [self.spaceship,
                        self.asteroids,
                        self.darkmatter,
                        self.lblScore,
                        self.bullet]
        
    def processEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                self.bullet.fire()
        
    def process(self):
        for asteroid in self.asteroids:
            if asteroid.collidesWith(self.spaceship):
                asteroid.reset()
                self.deathflash.play()
                print(f"Score: {self.score}")
                self.stop()
            if self.darkmatter.collidesWith(self.spaceship):
                self.darkmatter.reset()
                self.collect.play()
                self.score += 1
                self.lblScore.text = f"Score: {self.score}"
            if self.bullet.collidesWith(asteroid):
                asteroid.reset()
                self.deathflash.play()
                
class Instructions(simpleGE.Scene):
    def __init__(self, prevScore):
        super().__init__()
        
        self.prevScore = prevScore
        self.repsonse = "Quit"
        
        self.directions = simpleGE.MultiLabel()
        self.directions.textLines = [
        "You are aboard Earth Federation Spacecraft 1",
        "Tasked with collecting samples of dark matter",
        "spread through the universe",
        "However, enemy groups are also desiring the same material",
        "and are attempting to destroy you",
        "Collect as many samples as possible before",
        "you are destroyed by the incoming asteroids",
        "Move with the Up, Down, Left, and Right Arrow Keys",
        "Good Luck!"]
        
        self.directions.center = (320, 240)
        self.directions.size = (700, 300)
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Play (Up)"
        self.btnPlay.center = (100, 425)
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit (Down)"
        self.btnQuit.center = (535, 425)
        
        self.lblScore = simpleGE.Label()
        self.lblScore.text = "Last Score: 0"
        self.lblScore.center = (320, 425)
        
        self.lblScore.text = f"Last Score: {self.prevScore}"
        
        self.sprites = [self.directions,
                        self.btnPlay,
                        self.btnQuit,
                        self.lblScore]
    
    def process(self):
        if self.btnPlay.clicked:
            self.response = "Play"
            self.stop()
            
        if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop()
    
    def processEvent(self, event):
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.response = "Play"
                self.stop()
            
            if event.key == pygame.K_s:
                self.response = "Quit"
                self.stop()


            
def main():
    
    keepGoing = True
    lastScore = 0 
    while keepGoing:
        instructions = Instructions(lastScore)
        instructions.start()
        
        if instructions.response == "Play":
            game = Game()
            game.start()
            lastScore = game.score
            
        else:
            keepGoing = False
    
if __name__ == "__main__":
    main()
