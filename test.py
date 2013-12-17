#-*- coding: utf-8 -*-

import pygame
import sys
from pygame.locals import Color
from pygame.locals import K_LEFT as LEFT
from pygame.locals import K_DOWN as DOWN 
from pygame.locals import K_UP as UP
from pygame.locals import K_RIGHT as RIGHT

from screen.game import GameScreen
from screen.menu import MenuScreen

# Game init
pygame.init()
screen = pygame.display.set_mode((640,480))
ms = MenuScreen(640,480,pygame.Surface((640,480))) 
gs = GameScreen(640,480,pygame.image.load('img/Background.png').convert_alpha())

screen.blit(ms.surface, (0,0))
pygame.display.flip()
while 1:
    # Limit frame
    pygame.time.Clock().tick(30)

    # Catch event to quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ms.main_loop()
    pygame.display.update()
    screen.blit(ms.surface, (0,0))
    
