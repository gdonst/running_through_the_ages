import os
import pygame

#Class to display the score for the player
class Score:
    #Initialize the variables for the score
    def __init__(self, fontName='Gameplay.ttf'):
        self.value = 0
        self.font = pygame.font.Font(os.path.join('../fonts', fontName), 24)
        self.score = self.font.render(
            'SCORE : ' + str(self.value), True, (255, 255, 255))

    #Calling this function with an amount updates the current score for the player
    def updateScore(self, amount):
        self.value += amount
        self.score = self.font.render(
            'SCORE : ' + str(self.value), True, (255, 255, 255))

    #Draws the current score to the screen
    def draw(self, screen):
        screen.blit(self.score, (10, 10))


#class for changing and displaying the next level/age the player will see
class Level:
    #Initialize the variables for the level/age
    def __init__(self, fontName='Gameplay.ttf'):
        self.value = "1000"
        self.font = pygame.font.Font(os.path.join('../fonts', fontName), 24)
        self.score = self.font.render(
            'NEXT AGE : ' + str(self.value), True, (255, 255, 255))

    #Updates the number for the next level/age
    def updateLevel(self, amount):
        self.value = amount
        self.score = self.font.render(
            'NEXT AGE : ' + str(self.value), True, (255, 255, 255))

    #Draws the next level/age to the screen for the player to see
    def draw(self, screen):
        screen.blit(self.score, (1130, 10))


#Class for changing and displaying the current background image
class Background:
    #Initialize the variables for the background
    def __init__(self, bgName='titlescreen.png'):
        self.image = pygame.image.load(
            os.path.join("../assets/backgrounds", bgName))

    #Takes screen info and background sets it to the variable
    def setBackground(self, bgName, screenWidth, screenHeight):
        self.image = pygame.image.load(
            os.path.join('../assets/backgrounds', bgName))
        self.image = pygame.transform.scale(
            self.image, (screenWidth, screenHeight))

    #Draws the current next age/level number to the screen for the player to see
    def draw(self, screen):
        screen.blit(self.image, (0, 0))


class Sound:
    #Initialize the variables for the sound/music
    def __init__(self):
        #pygame.mixer.pre_init(44100, -16, 2, 2048)
        #pygame.mixer.init()
        self.lossSound = pygame.mixer.Sound(os.path.join('../sounds', 'loss.wav'))
        self.victorySound = pygame.mixer.Sound(os.path.join('../sounds', 'victory.wav')) 
        self.music = pygame.mixer.music.load(os.path.join('../sounds', 'menu.wav'))
        self.jump = pygame.mixer.Sound(os.path.join('../sounds', 'jump.wav')) 

    def startMusic(self, fileName='menu.wav'):
        pygame.mixer.music.load(os.path.join('../sounds', fileName))
        pygame.mixer.music.play(-1)