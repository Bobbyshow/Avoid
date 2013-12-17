#-*- coding: utf-8 -*-

import pygame
from exceptions import Exception

from screen.game import GameScreen
from screen.menu import MenuScreen
from screen.lib.base_screen import ChangeScreenException

# Game init
pygame.init()
screen = pygame.display.set_mode((640,480))
ms = MenuScreen(640,480,pygame.Surface((640,480))) 

main_screen = ms

screen.blit(main_screen.surface, (0,0))
pygame.display.flip()
while 1:
    # Limit frame
    pygame.time.Clock().tick(30)

    # Catch event to quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # Main loop execute and catch screen change
    try:
        main_screen.main_loop()
        pygame.display.update()
        screen.blit(main_screen.surface, (0,0))
    except ChangeScreenException as cse:
        print str(cse)
        if cse.value == 1:
            gs = GameScreen(640,480,pygame.image.load('img/Background.png').convert_alpha())
            main_screen = gs
            continue
        elif cse.value == 0:
            del gs
            main_screen = ms
            continue
        else:
            raise Exception('Problem during ChangeScreen. Check values')
    
