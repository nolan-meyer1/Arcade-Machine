# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 12:03:59 2024

@author: chris
"""

import random, pygame, simpleGE

#The boxes
class Cage(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("border.png")
        self.setSize(600, 350)
        self.position = (320, 235)

class ScoreBox(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("textBox.png")
        self.setSize(475, 70)
        self.position = (320, 50)

class PlayBox(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("textBox.png")
        self.setSize(200, 60)
        self.position = (100, 450)

class QuitBox(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("textBox.png")
        self.setSize(200, 60)
        self.position = (540, 450)

class Ship(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        
        self.setImage("ship.png")   
        self.setSize(70, 70)
        self.position = (320, 240)
        self.hitPoints = 10
        self.imageAngle = 90
        self.setBoundAction(self.STOP)
        
    def process(self):
        if self.isKeyPressed(pygame.K_a):
            self.imageAngle += 5
        if self.isKeyPressed(pygame.K_d):
            self.imageAngle -= 5
        if self.isKeyPressed(pygame.K_w):
            if self.right < self.screenWidth:
                if self.left > 0:
                    if self.top < self.screenHeight:
                        if self.bottom > 0:
                            self.forward(7)
        if self.isKeyPressed(pygame.K_s):
            self.forward(-7)
        

class Bullet(simpleGE.Sprite):
    def __init__(self, scene, parent):
        super().__init__(scene)
        self.parent = parent
        self.colorRect("white", (5,5))
        self.setBoundAction(self.HIDE)
        self.hide()
        
    def fire(self):
        self.show()
        self.position = self.parent.position
        self.moveAngle = self.parent.imageAngle
        self.speed = 20

class Meteor(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("entropy.png")
        self.setSize(50, 50)
        self.reset()


#have the meteors come from different sides and move at different angles
    def reset(self):
        side = random.randint(1, 4)
        if side == 1:
            self.y = 25
            self.x = random.randint(25, 615)
            self.moveAngle = random.randint(180, 360)
            self.speed = random.randint(3, 7)
            
        
        if side == 2:
            self.y = random.randint(25, 455)
            self.x = 615
            self.moveAngle = random.randint(90, 270)
            self.speed = random.randint(3,7)
        
        if side == 3:
            self.y = 455
            self.x = random.randint(25, 615)
            self.moveAngle = random.randint(0, 180)
            self.speed = random.randint(3, 7)
            
        if side == 4:
            self.y = random.randint(25, 455)
            self.x = 25
            self.moveAngle = random.randint(270, 450)
            self.speed = random.randint(3,7)


class Comet(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("comet.png")
        self.setSize(50, 50)
        self.reset()


#have the meteors come from different sides and move at different angles
    def reset(self):
        side = random.randint(1, 4)
        if side == 1:
            self.y = 25
            self.x = random.randint(25, 615)
            self.moveAngle = random.randint(180, 360)
            self.speed = random.randint(3, 7)
            
        
        if side == 2:
            self.y = random.randint(25, 455)
            self.x = 615
            self.moveAngle = random.randint(90, 270)
            self.speed = random.randint(3,7)
        
        if side == 3:
            self.y = 455
            self.x = random.randint(25, 615)
            self.moveAngle = random.randint(0, 180)
            self.speed = random.randint(3, 7)
            
        if side == 4:
            self.y = random.randint(25, 455)
            self.x = 25
            self.moveAngle = random.randint(270, 450)
            self.speed = random.randint(3,7)

#Game textboxes
class GameScore(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("textBox.png")
        self.setSize(200, 60)
        self.position = (100, 30)


class TimeBox(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("textBox.png")
        self.setSize(200, 60)
        self.position = (540, 30)

class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.clearBack = True
        self.fgColor = "white"
        self.text = "Score: 0"
        self.center = (100, 30)

class LblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.clearBack = True
        self.fgColor = "white"
        self.text = "Time Elapsed: 0"
        self.center = (540, 30)

class HealthBox(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("textBox.png")
        self.setSize(200, 60)
        self.position = (320, 30)

class LblHealth(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.clearBack = True
        self.fgColor = "white"
        self.text = "Health: 10"
        self.center = (320, 30)





class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setCaption("Survive within the confines of Ouroboros")
        self.background.fill((18, 22, 41))
        self.setImage("eventHorizon.png")
        
        self.ship = Ship(self)
        
        self.timer = simpleGE.Timer()
        
        pygame.mixer.music.load("Orbital Colossus.mp3")
        pygame.mixer.music.play()
        #Music track by Matthew Pablo on opengameart.org
        #self.sndBG = simpleGE.Sound("Orbital Colossus.mp3")
        #self.sndBG.play()
        
        self.sndHeal = simpleGE.Sound("17.mp3")
        #sound effect by Zoltan Milhayi on opengameart.org
        
        self.sndShoot = simpleGE.Sound("laser3.wav")
        #sound effect by dklon on opengameart.org
        
        self.sndExplode = simpleGE.Sound("laser11.wav")
        #sound effect by dklon on opengameart.org
        
        self.sndDamage = simpleGE.Sound("8bit_bomb_explosion.wav")
        #sound effect by Luke.RUSTLTD on opengameart.org
        
        
        self.score = 0
        self.gameScore = GameScore(self)
        self.lblScore = LblScore()
        
        self.healthBox = HealthBox(self)
        self.lblHealth = LblHealth()
        
        self.timeBox = TimeBox(self)
        self.lblTime = LblTime()
        
        self.numMeteors = 10
        self.numComets = 3
        
        self.comets = []
        for i in range(self.numComets):
            self.comets.append(Comet(self))
            
        
        self.meteors = []
        for i in range(self.numMeteors):
            self.meteors.append(Meteor(self))
        
        self.numBullets = 75
        self.currentBullet = 0
        
        self.bullets = []
        for i in range(self.numBullets):
            self.bullets.append(Bullet(self, self.ship))
        
        self.sprites = [self.ship, self.bullets, self.meteors, self.comets, self.timeBox, self.gameScore, self.lblTime, self.healthBox, self.lblHealth, self.lblScore]
    
    def process(self):
        for meteor in self.meteors:
            if self.ship.collidesWith(meteor):
                meteor.reset()
                self.ship.hitPoints -= 1
                self.sndDamage.play()
                self.lblHealth.text = f"Health: {self.ship.hitPoints}"
            
            for bullet in self.bullets:
                if bullet.collidesWith(meteor):
                    self.sndExplode.play()
                    self.score += 1
                    self.lblScore.text = f"Score: {self.score}"
                    meteor.reset()
        
        for comet in self.comets:
            if self.ship.collidesWith(comet):
                comet.reset()
                self.ship.hitPoints += 1
                self.sndHeal.play()
                self.lblHealth.text = f"Health: {self.ship.hitPoints}"
        
        self.lblTime.text = f"Time Passed:{self.timer.getElapsedTime():.0f}"
            
        if self.ship.hitPoints <= 0:
            self.stop()
    
    def processEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                self.currentBullet += 1
                if self.currentBullet >= self.numBullets:
                    self.currentBullet = 0
                self.bullets[self.currentBullet].fire()
                self.sndShoot.play()


class Instructions(simpleGE.Scene):
    def __init__(self, score = 0):
        super().__init__()
        self.setImage("night.PNG")
        
        self.status = "quit"
        self.score = score
        
        self.sndPress = simpleGE.Sound("laser7.wav")
        #sound effect by dklon on opengameart.org
        
        pygame.mixer.music.load("Space Music.mp3")
        #music by Hitctrl on opengameart.org
        pygame.mixer.music.play()
        
        self.cage = Cage(self)
        self.playBG = PlayBox(self)
        self.quitBG = QuitBox(self)
        self.scoreBox = ScoreBox(self)
        
        self.Instructions = simpleGE.MultiLabel()
        self.Instructions.clearBack = True
        self.Instructions.fgColor = "black"
        self.Instructions.textLines = [
            "Survive within the void.",
            "Shoot the meteors with 'red'",
            "Movement with joystick"
            ]
        
        self.Instructions.center = (320, 240)
        self.Instructions.size = (450, 200)
        
        self.lblScore = simpleGE.Label()
        self.lblScore.clearBack = True
        self.lblScore.fgColor = "white"
        self.lblScore.center = (320, 50)
        self.lblScore.size = (400, 30)
        self.lblScore.text = f"Previous Score: {self.score}"
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.clearBack = True
        self.btnPlay.fgColor = "white"
        self.btnPlay.center = (100, 450)
        self.btnPlay.text = "Play (up)"
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.clearBack = True
        self.btnQuit.fgColor = "white"
        self.btnQuit.center = (540, 450)
        self.btnQuit.text = "Quit (down)"
        
        self.sprites = [self.scoreBox, self.cage, self.playBG, self.quitBG, self.lblScore, self.Instructions, self.btnPlay, self.btnQuit]
        
        
    def process(self):
        if self.btnPlay.clicked:
            self.status = "play"
            self.sndPress.play()
            self.stop()
        if self.btnQuit.clicked:
            self.status = "quit"
            self.sndPress.play()
            self.stop()
            
        if self.isKeyPressed(pygame.K_w):
            self.status = "play"
            self.sndPress.play()
            self.stop()
        if self.isKeyPressed(pygame.K_s):
            self.status = "quit"
            self.sndPress.play()
            self.stop()

def main():
    pygame.display.set_caption("Reside within the eternal loop and try to survive.")


    keepGoing = True
    score = 0
    while keepGoing:
        instructions = Instructions(score)
        instructions.start()
    
        if instructions.status == "play":
            game = Game()
            game.start()
            score = game.score
        else:
            keepGoing = False

    
if __name__ == "__main__":
    main()