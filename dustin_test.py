import pygame
import random
from os import path

# path.dirname : gets path of current directory that this file is located in by passing __file__. (__file__ is the current running python module) . 
# 
# path.join : 

img_dir2 = path.join(path.dirname(__file__), 'img2')



WIDTH = 600
HEIGHT = 480
FPS = 60

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Initialize pygame and create window
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SubwayFighter")
clock = pygame.time.Clock()



def show_menu_screen():
    screen.blit(intro_background2, intro_background_rect2)
    # draw_text(screen, "THIS IS THE MENU SCREEN", 64, WIDTH / 2, HEIGHT / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # Any key press will start the game
            if event.type == pygame.KEYDOWN:
                waiting = False
def maingame():
    screen.blit(main_background, main_background_rect2)
    # draw_text(screen, "THIS IS THE MENU SCREEN", 64, WIDTH / 2, HEIGHT / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # Any key press will start the game
            if event.type == pygame.KEYDOWN:
                waiting = False


intro_background2 = pygame.image.load(path.join(img_dir2, 'menu.png')).convert()
intro_background_rect2 = intro_background2.get_rect()
main_background = pygame.image.load(path.join(img_dir2, 'maingame.png')).convert()
main_background_rect2 = main_background.get_rect()

show_menu_screen()
maingame()