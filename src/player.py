import os
import pygame

#Initializing vector for player movement
vec = pygame.math.Vector2

class Player:
    #Initialize player
    def __init__(self, floor, currentLevel, imageName='caveman.png'):
        self.floor = floor
        self.currentLevel = currentLevel
        self.image = pygame.image.load(
            os.path.join('../assets/player', imageName)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.width = 110
        if currentLevel == 3:
            self.rect.width = 50
        self.pos = vec(200, 601)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    #For changing the image of the player
    def set_image(self, imageName):
        self.image = pygame.image.load(
            os.path.join('../assets/player', imageName)).convert_alpha()
    
    #For changing the current level (age) of the game
    def set_currentLevel(self, currentLevel):
        self.currentLevel = currentLevel

    #Drawing the player itself, and the movement of the player based on user input
    def draw(self, screen):
        #gravity variable
        self.acc = vec(0, 0.5)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -1
        if keys[pygame.K_RIGHT]:
            self.acc.x = 1
        if keys[pygame.K_SPACE]:
            collision = self.rect.colliderect(self.floor)
            if collision:
                self.vel.y = -15

        #Apply friction
        self.acc.x += self.vel.x * -0.12
        #Equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        #Barriers at side of screen
        if self.pos.x > 1350:
            self.pos.x = 1350
        if self.pos.x < 50:
            self.pos.x = 50

        self.rect.midbottom = self.pos

        screen.blit(self.image, self.rect)