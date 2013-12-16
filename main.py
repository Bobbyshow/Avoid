#-*- coding: utf-8 -*-

import pygame
import sys
from pygame.locals import Color
from pygame.locals import K_LEFT as LEFT
from pygame.locals import K_DOWN as DOWN 
from pygame.locals import K_UP as UP
from pygame.locals import K_RIGHT as RIGHT

from pygame.sprite import RenderUpdates as Group
from entity.hero import Hero
from entity.barrier import Barrier
from entity.missile import Missile

# Game init
pygame.init()
screen = pygame.display.set_mode((640,480))

# Game entities init
player = Hero('player', (320,240,15,15), [2,2], 4, 3, '../apps/Joueur.png')
barrier = []
barrier.append(Barrier('barrier', (259,160,121,20), [2,2], 2, 0, '../apps/Barriere.png'))
barrier[0].direction_set(UP)
barrier.append(Barrier('barrier', (259,300,121,20), [2,2], 2, 0, '../apps/Barriere.png'))
barrier[1].direction_set(DOWN)
missile = []
missile.append(Missile('missile', (100,300,22,43), [3,1], 3, 0, '../apps/Missile.png'))
missile[0].direction_set(UP)
missile.append(Missile('missile', (-10,240,43,22), [3,3], 3, 0, '../apps/Missile.png'))
missile[1].direction_set(RIGHT)
missile.append(Missile('missile', (650,300,43,22), [3,3], 3, 0, '../apps/Missile.png'))
missile[2].direction_set(LEFT)
missile.append(Missile('missile', (260,-10,22,43), [3,3], 3, 0, '../apps/Missile.png'))
missile[3].direction_set(DOWN)

grp = Group()
barrier_grp = Group()
missile_grp = Group()

background = pygame.image.load('../apps/Background.png').convert_alpha()
background_rect = background.get_rect()

screen.blit(
    background, background_rect
)

missile_grp.add(missile)
missile_grp.update()
missile_grp.draw(screen)

barrier_grp.add(barrier)
barrier_grp.update()
barrier_grp.draw(screen)

grp.add(player)
grp.update()
grp.draw(screen)

pygame.display.flip()

while 1:
    # Limit frame
    pygame.time.Clock().tick(10)
    # Catch event to quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    for sprite_missile in missile_grp.sprites():
        sprite_missile.setup_collapse()
    for sprite_missile in grp.sprites():
        sprite_missile.setup_collapse()
    for sprite_missile in barrier_grp.sprites():
        sprite_missile.setup_collapse()

    # Check collapse between sprite
    collapse_sprite = pygame.sprite.spritecollide(player, missile_grp, True)
    if collapse_sprite != []:
        player.lose_life()
        print player.is_alive()
        if not player.is_alive():
            player.remove(grp)
        print collapse_sprite
    
    # Check collapse :: barrier vs player
    # If touch, you Die !!!
    collapse_sprite = pygame.sprite.spritecollide(player, barrier_grp, False)
    if collapse_sprite != []:
        # Make loss animation
        continue
    
    # Print the background (To erase all map)
    screen.blit(
        background, background_rect
    )

    # Check key pressed and move if it's true
    # Or stop move
    if pygame.key.get_pressed()[LEFT] == 1:
        movement_direction = LEFT
        grp.update(LEFT)
    elif pygame.key.get_pressed()[RIGHT] == 1:
        movement_direction = RIGHT
        grp.update(RIGHT)
    elif pygame.key.get_pressed()[UP] == 1:
        movement_direction = UP
        grp.update(UP)
    elif pygame.key.get_pressed()[DOWN] == 1:
        movement_direction = DOWN
        grp.update(DOWN)
    else:
        grp.update()
    
    barrier_grp.update()
    missile_grp.update()
    
    
    ######## TESTING PART FOR HITBOX ########
    for sprite_missile in missile_grp.sprites():        
        screen.fill(pygame.Color(255,0,0),sprite_missile.get_rect(2))
    for sprite_missile in grp.sprites():
        screen.fill(pygame.Color(0,255,0),sprite_missile.get_rect(2))
    for sprite_missile in barrier_grp.sprites():
        screen.fill(pygame.Color(0,0,255),sprite_missile.get_rect(2))

    list_draw =  (
        grp.draw(screen) +
        barrier_grp.draw(screen) +
        missile_grp.draw(screen)
    )
    
    #screen.fill(pygame.Color(0,0,0), move_rect)
    pygame.display.update(list_draw)
