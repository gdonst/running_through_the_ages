import os
import pygame

#For when the game ends, display all end game variables such as high score
def gameover(screen, score, highscore):
    font = pygame.font.Font(os.path.join('../fonts', 'Gameplay.ttf'), 28)
    
    gameover_surface = font.render('GAME OVER press N to restart', True, (255, 255, 255))
    gameover_rect = gameover_surface.get_rect(center=(1400/2, 400))
    score_surface = font.render(f"Score: {int(score)}", True, (255,255,255))
    score_rect = score_surface.get_rect(center=(1400/2, 300)) 
    high_score_surface = font.render(f"High Score: {int(highscore)}", True, (255,255,255)) 
    high_score_rect = high_score_surface.get_rect(center=(1400/2, 350))

    screen.blit(score_surface, score_rect) 
    screen.blit(high_score_surface, high_score_rect)
    screen.blit(gameover_surface, gameover_rect)