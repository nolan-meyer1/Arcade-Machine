# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 10:17:08 2024

@author: bluet
"""
import simpleGE, pygame, math

class Game(simpleGE.Scene):
    def __init__(self,size):
        super().__init__(size)
        self.lapTime = False
        self.regTime = False
        self.background.fill("gray")
        self.car = Car(self)
        self.obstacles = []
        for i in range(21):
            newObstacle = Obstacles(self)
            newObstacle.y = 25
            newObstacle.x = (i * 50)
            self.obstacles.append(newObstacle)
        for i in range(21):
            newObstacle = Obstacles(self)
            newObstacle.y = 725
            newObstacle.x = (i * 50)
            self.obstacles.append(newObstacle)
        for i in range(16):
            newObstacle = Obstacles(self)
            newObstacle.y = (i * 50)
            newObstacle.x = 25
            self.obstacles.append(newObstacle)
        for i in range(16):
            newObstacle = Obstacles(self)
            newObstacle.y = (i * 50)
            newObstacle.x = 975
            self.obstacles.append(newObstacle)
        for i in range(3):
            newObstacle = Obstacles(self)
            newObstacle.y = 150 - (i * 50)
            newObstacle.x = 500
            self.obstacles.append(newObstacle)
        for i in range(10):
            newObstacle = Obstacles(self)
            newObstacle.y = 400
            newObstacle.x = 250 + (i * 50)
            self.obstacles.append(newObstacle)
        for i in range(3):
            newObstacle = Obstacles(self)
            newObstacle.y = 250 + (i * 50)
            newObstacle.x = 250
            self.obstacles.append(newObstacle)
        for i in range(3):
            newObstacle = Obstacles(self)
            newObstacle.y = 300 + (i * 50)
            newObstacle.x = 750
            self.obstacles.append(newObstacle)
        self.checkpoint = []
        for i in range(4):
            newCheckpoint = Checkpoint(self)
            newCheckpoint.y = 200 + (i * 50)
            newCheckpoint.x = 500
            self.checkpoint.append(newCheckpoint)
        self.checkpoint2 = []
        for i in range(4):
            newCheckpoint = Checkpoint2(self)
            newCheckpoint.y = 400
            newCheckpoint.x = 50 + (i * 50)
            self.checkpoint2.append(newCheckpoint)
        self.checkpoint3 = []
        for i in range(6):
            newCheckpoint = Checkpoint3(self)
            newCheckpoint.y = 450 + (i * 45)
            newCheckpoint.x = 500
            self.checkpoint3.append(newCheckpoint)
        self.checkpoint4 = []
        for i in range(5):
            newCheckpoint = Checkpoint4(self)
            newCheckpoint.y = 400
            newCheckpoint.x = 750 + (i * 45)
            self.checkpoint4.append(newCheckpoint)
        self.lblLapCount = lblLapCount(self)
        self.lblTimer = lblTimer(self)
        self.lblInstructions = lblInstructions(self)
        self.time = 0
        self.sprites = [self.checkpoint, self.checkpoint2, self.checkpoint3, self.checkpoint4, self.car, self.obstacles, self.lblLapCount, self.lblTimer, self.lblInstructions]
    def process(self):
        self.lblLapCount.text = f"Lap: {self.car.lap}"
        self.lblTimer.text = f"Time: {self.time:.1f}"
        if self.isKeyPressed(pygame.K_f):
            self.time = 0
            self.lapTime = False
            self.regTime = True
        if self.regTime:
            self.time += (1/30)
        if self.isKeyPressed(pygame.K_e):
            self.regTime = False
            self.lapTime = True
            self.time = 0
            self.lap = self.car.lap + 1
        if self.lapTime:
            keepGoing = True
            if self.lap != self.car.lap:
                keepGoing = False
            if keepGoing:
                self.time += (1/30)
        if self.isKeyPressed(pygame.K_z):
            self.regTime = False
            self.lapTime = False
            self.time = 0
        
class Obstacles(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.colorRect("blue",(50,50))
class Checkpoint(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.colorRect("white",(50,50))
class Checkpoint2(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.colorRect("white",(50,50))
class Checkpoint3(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.colorRect("white",(50,50))
class Checkpoint4(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.colorRect("white",(50,50))
class Car(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.angle = -90
        self.setImage("car.png")
        self.setAngle(self.angle)
        self.setSize(50, 30)
        self.drag = .94
        self.accel = 1.5
        self.turnRate = 6.5
        self.grip = .9
        self.lap = 0
        self.checkpointActive = False
        self.checkpoint2Active = False
        self.checkpoint3Active = False
        self.checkpoint4Active = True
        self.x = 600
        self.y = 250
        
    def process(self):
        speed = math.sqrt(self.dx*self.dx+(self.dy*self.dy))
        if self.isKeyPressed(pygame.K_a):
            self.imageAngle += self.turnRate
        if self.isKeyPressed(pygame.K_d):
            self.imageAngle -= self.turnRate            
        if self.isKeyPressed(pygame.K_w):
            self.addForce(self.accel * self.grip, self.imageAngle)
            if abs(speed) >= 12:
                if self.drag >= .85:
                    self.drag -= .001
            if abs(speed) < 12:
                if self.drag < .94:
                    self.drag += .001
        self.dx *= self.drag
        self.dy *= self.drag
        for obstacle in self.scene.obstacles:
            if self.collidesWith(obstacle):
                self.dx *= -.5
                self.dy *= -.5
                self.x += 3*self.dx
                self.y += 3*self.dy
                if self.collidesWith(obstacle):
                    self.x += 3*self.dx
                    self.y += 3*self.dy
                    if self.collidesWith(obstacle):
                        self.x += 3*self.dx
                        self.y += 3*self.dy
        for checkpoint2 in self.scene.checkpoint2:
            if self.checkpoint2Active:
                if self.collidesWith(checkpoint2):
                    self.checkpoint3Active = True
                    self.checkpoint2Active = False
        for checkpoint in self.scene.checkpoint:
            if self.checkpointActive:
                if self.collidesWith(checkpoint):
                    self.lap +=1
                    self.checkpointActive = False
                    self.checkpoint2Active = True
        for checkpoint3 in self.scene.checkpoint3:
            if self.checkpoint3Active:
                if self.collidesWith(checkpoint3):
                    self.checkpoint4Active = True
                    self.checkpoint3Active = False
        for checkpoint4 in self.scene.checkpoint4:
            if self.checkpoint4Active:
                if self.collidesWith(checkpoint4):
                    self.checkpointActive = True
                    self.checkpoint4Active = False
class lblLapCount(simpleGE.Label):
    def __init__(self, scene):
        super().__init__()
        self.text = "Lap: 0"
        self.center = (125, 25)
class lblTimer(simpleGE.Label):
    def __init__(self, scene):
        super().__init__()
        self.text = "Time: 0.0"
        self.center = (875, 25)
class lblInstructions(simpleGE.Label):
    def __init__(self, scene):
        super().__init__()
        self.text = "Red: start time White: lap time Yellow: reset time"
        self.size = (500, 30)
        self.center = (500, 25)
def main():
    game = Game((1000,750))
    game.start()
    
if __name__ == "__main__":
    main()