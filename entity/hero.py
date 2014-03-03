#-*- coding: utf-8 -*-

from lib.base_entity import BaseEntity
from lib.base_animation import BaseAnimation
from life import Life

from pygame.locals import K_UP as UP


class HeroAnimation(BaseAnimation):
    """Custom class Animation : HeroAnimation

    """
    WIDTH_SPRITE = 31 
    HEIGHT_SPRITE = 31
    
    def get_sprite(self, move_direction):
        direction_num = move_direction - UP
        frame =  self.subsurface(
            self.frame * self.WIDTH_SPRITE,
            direction_num * self.HEIGHT_SPRITE,
            self.WIDTH_SPRITE, 
            self.HEIGHT_SPRITE
        ).convert_alpha()
        return frame
        
class Hero(BaseEntity):
    """Custom class Entity : Hero
    
    Entity for the player. Represents the player
    and player's move
    """

    def __init__(self, rect_data):
        super(Hero, self).__init__(
            name='Hero',
            rect_data=rect_data,
            speed=[2,2],
            max_frame=4, 
            max_frame_delay=3, 
            img='img/Joueur.png'
        )
        self.life = 3
        self.add_child([
            Life((20,20,16,17)),
            Life((40,20,16,17)),
            Life((60,20,16,17))
        ])

    def init_animation(self, max_frame, max_frame_delay, img):
        return HeroAnimation(max_frame, max_frame_delay, img)
        
    def is_alive(self):
        """Return true if player is alive"""
        return self.life > 0
    
    def lose_life(self):
        """Remove 1 to life and remove 1 life sprite"""
        self.life = self.life - 1
        self.childs.sprites()[0].kill()
