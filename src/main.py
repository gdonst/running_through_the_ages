import sys
import pygame

# Modules to import
from player import Player
from obstacle import Obstacle
from utility import Score, Background, Sound, Level
from helper import gameover

pygame.init()

# Game Screen and font
width, height = 1400, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Running Through the Ages')
basic_font = pygame.font.Font('freesansbold.ttf', 32)
game_font = pygame.font.Font('../fonts/Gameplay.ttf', 40)

# Game Speed
clock = pygame.time.Clock()
vec = pygame.math.Vector2

# Colors
light_grey = (200,200,200)
dark_grey = (100,100,100)
black = (0,0,0)
white = (255,255,255)
bg_color = pygame.Color('grey12')

# Level and other important level variables
currentLevel = 1
game_active = True
soundCount = 0
imageSet = 0

# Obstacles and timer for obstacle spawning
obstacle_list = []
SPAWNOBSTACLE = pygame.USEREVENT #create a new event for adding a obstacle
pygame.time.set_timer(SPAWNOBSTACLE, 2500) #create a timer for 2.5s

# Background
background = Background()

# Score and level/age target
score = Score()
highscore = 0
level = Level()

# Floor
floor_surface = pygame.image.load('../assets/backgrounds/base.png')
floor_surface = pygame.transform.scale2x(floor_surface)
floor = pygame.Rect(0,600,1400,20)
floor_x_pos = 0

# Player
player1 = Player(floor, currentLevel)

# Sound
sound = Sound()
sound.startMusic()

#button for the main menu
def button(msg, x, y, w, h, inactive_color, active_color, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #if mouse is hovering on rectangle, draw as different color
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(screen, active_color, (x, y, w, h))
            if click[0] == 1 and action !=None:
                if action == 'play':
                    main()
                elif action == 'quit':
                    pygame.quit()
                    sys.exit()
        else:
            pygame.draw.rect(screen, inactive_color, (x, y, w, h))
        
        # Button text
        play_text = game_font.render(msg,False,bg_color)
        screen.blit(play_text,(x+45,y+10))

#Draws the floor to the screen where the player walks on
def draw_floor():
    screen.blit(floor_surface, (floor_x_pos,600))
    screen.blit(floor_surface, (floor_x_pos + 1400 ,600)) 

#Moves the obstables to the left at different speeds depending on the current level/age
def move_obstacles(obstacles):
    for obstacle in obstacles:
        if currentLevel == 1:
            obstacle.move(4)
        elif currentLevel == 2:
            obstacle.move(6)
        elif currentLevel == 3:
            obstacle.move(8)
        elif currentLevel == 4:
            obstacle.move(10)

#Draws the obstacles to the screen
def draw_obstacles(obstacles):
    for obstacle in obstacles:
        obstacle.draw(screen)

#Main menu before game starts
def game_intro():
	intro = True

    #While on the main menu
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		
		# Screen and title
		background.draw(screen)
		large_font = pygame.font.Font('../fonts/Gameplay.ttf', 65)
		title_text = large_font.render('Running Through the Ages',False,white)
		screen.blit(title_text,((160),(height/4)))

        #Calls button class to make buttons for play and quit
		button('Play', (width-210)/2, 300, 210, 70, light_grey, dark_grey, 'play')
		button('Quit', (width-210)/2, 380, 210, 70, light_grey, dark_grey, 'quit')

		# Loop Timer
		pygame.display.flip()
		clock.tick(60)

#when the user loses or hits an obstacle this game reset can be called and it will reset every important game variable
def game_reset():
    global game_active
    global currentLevel
    global soundCount

    game_active = True
    obstacle_list.clear() 
    score.value = 0
    level.updateLevel("1000")
    player1.pos = vec(200,601)
    currentLevel = 1
    soundCount = 0
    pygame.time.set_timer(SPAWNOBSTACLE, 2500)
    statemanager()

#State manager for each level/age
def statemanager():
    global currentLevel
    global imageSet

    #If for each level
    if(currentLevel == 1):
        #Change background
        background.setBackground('age1.png', width, height)
        #If statement so that it only sets the image once
        if imageSet == 0:
            player1.set_image('caveman.png')
            imageSet += 1
        #Tells the player class what the current level is
        player1.set_currentLevel(1)
        #Starts the game
        main_game(4,1)
    if(currentLevel == 2):
        background.setBackground('age2.png', width, height)
        if imageSet == 0:
            player1.set_image('knight.png')
            imageSet += 1
        player1.set_currentLevel(2)
        main_game(4,1)
    if(currentLevel == 3):
        background.setBackground('age3.png', width, height)
        if imageSet == 0:
            player1.set_image('businessman.png')
            imageSet += 1
        player1.set_currentLevel(3)
        main_game(4,1)
    if(currentLevel == 4):
        background.setBackground('age4.png', width, height)
        if imageSet == 0:
            player1.set_image('astronaut.png')
            imageSet += 1
        player1.set_currentLevel(4)
        main_game(4,1)

#Main game function
def main_game(spd, scorepoint):
    global currentLevel
    global floor_x_pos
    global game_active
    global highscore
    global soundCount
    global imageSet

    # Game Events
    for event in pygame.event.get():
                
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
           
        #detect new obstacle event
        if event.type == SPAWNOBSTACLE:
            obstacle = Obstacle()
            #changes the obstacle image based on the current level/age
            if currentLevel == 1:
                obstacle.set_image('rock_A1.png')
            elif currentLevel == 2:
                obstacle.set_image('tower_A2.png')
            elif currentLevel == 3:
                obstacle.set_image('barricade_A3.png')
            elif currentLevel == 4:
                obstacle.set_image('spaceship_A4.png')
            obstacle_list.append(obstacle)
            
        #Keyboard events for player input
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            #If statements to change image direction based on the way the user pressed the arrow keys
            if keys[pygame.K_LEFT]:
                if currentLevel == 1:
                    player1.set_image("cavemanL.png")
                elif currentLevel == 2:
                    player1.set_image("knightL.png")
                elif currentLevel == 3:
                    player1.set_image("businessmanL.png")
                elif currentLevel == 4:
                    player1.set_image("astronautL.png")
            if keys[pygame.K_RIGHT]:
                if currentLevel == 1:
                    player1.set_image("caveman.png")
                elif currentLevel == 2:
                    player1.set_image("knight.png")
                elif currentLevel == 3:
                    player1.set_image("businessman.png")
                elif currentLevel == 4:
                    player1.set_image("astronaut.png")
            #Play a jump sound when the user jumps
            if event.key == pygame.K_SPACE:
                sound.jump.play()
            #Resets the game when the user enters n on the end screen
            if event.key == pygame.K_n and game_active == False: 
                game_reset()

    #If the player collides with the floor make sure they stay on top of it
    if player1.rect.colliderect(floor):
        player1.pos.y = (floor.top) + 1
        player1.vel.y = 0

    #For each obstacle in the obstacle list check for collision, if collision then end game
    for obstacle in obstacle_list:
        if player1.rect.colliderect(obstacle):
            game_active = False

    # Draw Background to Screen
    background.draw(screen)

    #If the game is currently marked as active
    if game_active: 
        pygame.draw.rect(screen,black,floor)

        # Player
        player1.draw(screen)

        # Score
        score.updateScore(scorepoint)
        score.draw(screen)

        #Change the next age/level display based on the current level
        if currentLevel == 1:
            level.draw(screen)
        elif currentLevel == 2:
            level.updateLevel("2000")
            level.draw(screen)
        elif currentLevel == 3:
            level.updateLevel("3000")
            level.draw(screen)
        elif currentLevel == 4:
            level.updateLevel("Infinite")
            level.draw(screen)

        # Obstacle Movement
        move_obstacles(obstacle_list)
        draw_obstacles(obstacle_list)

        #This section will initiate the obstacle speed changes, music, and change the level... in other words age up.
        if score.value == 1:
            sound.startMusic("age1.wav")
            imageSet = 0
            level.draw(screen)
        if score.value == 1000:
            pygame.time.set_timer(SPAWNOBSTACLE, 2000) #create a timer for 2s
            sound.startMusic("age2.wav")
            imageSet = 0
            currentLevel += 1
        if score.value == 2000:
            pygame.time.set_timer(SPAWNOBSTACLE, 1500) #create a timer for 1.5s
            sound.startMusic("age3.wav")
            imageSet = 0
            currentLevel += 1
        if score.value == 3000:
            pygame.time.set_timer(SPAWNOBSTACLE, 1250) #create a timer for 1.25s
            sound.startMusic("age4.wav")
            imageSet = 0
            currentLevel += 1

        #Draws the floor to the screen
        draw_floor()

        # Floor Movement
        floor_x_pos -= 2

        if floor_x_pos <= -1400:
            floor_x_pos = 0

    #For when the game ends and isn't running
    else:
        #Stops music
        pygame.mixer.music.stop()
        #Update score if there is a new high score and play a vitory sound
        if score.value >= highscore:
            highscore = score.value
            if soundCount == 0:
                sound.victorySound.play()
                soundCount += 1
        #if there is no new high score play a loss sound
        else:
            if soundCount == 0:
                sound.lossSound.play()
                soundCount += 1

        #Initiate the ending game over screen
        gameover(screen, score.value, highscore)

    # Update Game
    pygame.display.update()

#Main execution from main menu that launches the state manager and thus the game
def main():
    while True:
        # FPS
        clock.tick(60)
        statemanager()

#Lanuches menu when the application is run
game_intro()
