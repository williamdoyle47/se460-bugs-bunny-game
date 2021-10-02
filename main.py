import pygame
import os
import random
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
CHAR_HEIGHT, CHAR_WIDTH = 100,100 


BUGS_IMAGE = pygame.image.load(
    os.path.join('assets', 'bugs.png')).convert_alpha()
BUGS = pygame.transform.scale(BUGS_IMAGE,(CHAR_HEIGHT, CHAR_WIDTH))
BUGS_RECT = BUGS.get_rect(center=([random.randint(100, 800),random.randint(100, 700)]))

TAZ_IMAGE = pygame.image.load(
        os.path.join('assets', 'taz.png')).convert_alpha()
TAZ = pygame.transform.scale(TAZ_IMAGE,  (CHAR_HEIGHT, CHAR_WIDTH))
TAZ_RECT = TAZ.get_rect(center=([random.randint(100, 800),random.randint(100, 700)]))

TWEETY_IMG = pygame.image.load(
        os.path.join('assets', 'tweety.png')).convert_alpha()
TWEETY = pygame.transform.scale(TWEETY_IMG,  (CHAR_HEIGHT, CHAR_WIDTH))
TWEETY_RECT = TWEETY.get_rect(center=([random.randint(100, 800),random.randint(100, 700)]))

MARVIN_IMG = pygame.image.load(
        os.path.join('assets', 'marvin.png')).convert_alpha()
MARVIN = pygame.transform.scale(MARVIN_IMG,  (CHAR_HEIGHT, CHAR_WIDTH))
MARVIN_RECT = MARVIN.get_rect(center=([random.randint(100, 800),random.randint(100, 700)]))

def move(player, player_rect):
    x = random.randint(100,760)
    y = random.randint(100,760)
    player_rect.move_ip(x,y)
    WIN.blit(player,player_rect)
    pygame.display.flip()

def main():
    run = True
    moves = 20

    WIN.blit(BUGS, BUGS_RECT)
    WIN.blit(TAZ, TAZ_RECT)
    WIN.blit(TWEETY, TWEETY_RECT)
    WIN.blit(MARVIN, MARVIN_RECT)
    pygame.display.flip()
    
    while run:
        count = 0
        while (count <= moves):
            pygame.time.wait(2000)
            move(BUGS, BUGS_RECT)
            move(TAZ, TAZ_RECT)
            move(TWEETY, TWEETY_RECT)
            move(MARVIN, MARVIN_RECT)
            
        
    

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

main()