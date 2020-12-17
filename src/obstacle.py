import os
import random
import pygame


class Obstacle:
    #Initialize the obstacle object
    def __init__(self, imageName='rock_A1.png'):
        self.image = pygame.image.load(
            os.path.join('../assets/obstacle', imageName)).convert()
        self.rect = self.image.get_rect() #add a rect object for the obstacle
        self.posX = 1400
        #set a random height for the obstacle
        self.posY = random.randint(425, 550)
        self.moveX = -1 
        self.speed = 3

    #Setting a new image for the obstacle
    def set_image(self, imageName):
        self.image = pygame.image.load(
            os.path.join('../assets/obstacle', imageName))

    #Moving the obstacle with a set speed
    def move(self, speednum):
        self.speed = speednum
        self.posX += self.moveX * self.speed

    #Drawing the obstacle
    def draw(self, screen):
        self.rect.midtop = (self.posX, self.posY)
        screen.blit(self.image, self.rect)