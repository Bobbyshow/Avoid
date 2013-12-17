#-*- coding: utf-8 -*-

import pygame.image

from entity.hero import Hero
from entity.barrier import Barrier
from entity.missile_generator import MissileGenerator
from entity.missile import Missile
from lib.base_screen import BaseScreen, ChangeScreenException

from pygame.locals import K_LEFT as LEFT
from pygame.locals import K_DOWN as DOWN 
from pygame.locals import K_UP as UP
from pygame.locals import K_RIGHT as RIGHT

from pygame.surface import Surface
from pygame.sprite import RenderUpdates as Group

class GameScreen(BaseScreen):
    """ Screen inherit from BaseScreen.
    
    Game's screen.
    """
    __hitbox_test = True
    
    def init_entities_after(self, surface):
        #Group player
        self.grp = Group()
        player = Hero(
            'player',
            (320,240,15,15),
            [2,2],
            4,
            3,
            'img/Joueur.png'
        )
        
        self.grp.add(player)
        self.grp.update()
        self.grp.draw(surface)
        #self.grp = grp

        #Group barrier
        barrier = []
        barrier.append(
            Barrier(
                'barrier',
                (259,160,121,20),
                [2,2],
                2,
                0,
                'img/Barriere.png'
            )
        )
        barrier[0].direction_set(UP)
        barrier.append(
            Barrier(
                'barrier',
                (259,300,121,20),
                [2,2],
                2,
                0,
                'img/Barriere.png'
            )
        )
        barrier[1].direction_set(DOWN)
        
        grp_barrier = Group()
        grp_barrier.add(barrier)
        grp_barrier.update()
        grp_barrier.draw(surface)
        self.grp_barrier = grp_barrier

        # Missile Generator
        self.miss_gen =  MissileGenerator()
        self.grp_missile = Group()

    def execute(self, surface):
        # Check collapse
        self.check_collapse()
        # Check missile's group
        missile = self.miss_gen.check_generation()
        if missile is not None:
            self.grp_missile.add(missile)
        self.grp_missile.update()
        # Check barrier's move
        self.grp_barrier.update()
        # Check player's move        
        if pygame.key.get_pressed()[LEFT] == 1:
            movement_direction = LEFT
            self.grp.update(LEFT)
        elif pygame.key.get_pressed()[RIGHT] == 1:
            movement_direction = RIGHT
            self.grp.update(RIGHT)
        elif pygame.key.get_pressed()[UP] == 1:
            movement_direction = UP
            self.grp.update(UP)
        elif pygame.key.get_pressed()[DOWN] == 1:
            movement_direction = DOWN
            self.grp.update(DOWN)
        else:
            self.grp.update()

    def draw(self, surface):
        # Testing hitbox part
        if self.__hitbox_test:
            for sprite in self.grp.sprites():
                surface.fill(pygame.Color(0,255,0),sprite.get_rect(2))
            for sprite in self.grp_barrier.sprites():
                surface.fill(pygame.Color(0,0,255),sprite.get_rect(2))
            for sprite in self.grp_missile.sprites():        
                surface.fill(pygame.Color(255,0,0),sprite.get_rect(2))

        return (
            self.grp.draw(surface) +
            self.grp_barrier.draw(surface) +
            self.grp_missile.draw(surface)
        )
        
    def check_collapse(self):
        for sprite in (
            self.grp.sprites() + 
            self.grp_missile.sprites() + 
            self.grp_barrier.sprites()):
            
            sprite.setup_collapse()
        # Check collapse with player and missile
        player = self.grp.sprites()[0]
        collapse_sprite = pygame.sprite.spritecollide(player, self.grp_missile, True)
        for sprite in collapse_sprite:
            del sprite
            player.lose_life()

        # Check collapse :: barrier vs player
        collapse_sprite = pygame.sprite.spritecollide(
            player,
            self.grp_barrier, False
        )
        for sprite in collapse_sprite:
            player.lose_life()
            
        if not player.is_alive():
            player.kill()
            del player
            raise ChangeScreenException(0,'You lose the game')
        

    """
    def erase_all_map(self):
    bg = pygame.image.load(self.background).convert_alpha()
    self.grp.clear(self.surface, bg)
    self.grp_missile.clear(self.surface, bg)
    self.grp_barrier.clear(self.surface, bg)
    """    
