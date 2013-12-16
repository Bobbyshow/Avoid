#-*- coding: utf-8 -*-

from lib.base_entity import BaseEntity
from lib.base_animation import BaseAnimation
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

    def __init__(self, name, rect_data, speed, max_frame, max_frame_delay, img):
        super(Hero, self).__init__(name, rect_data, speed, max_frame, max_frame_delay, img)
        self.life = 1
        
    def init_animation(self, max_frame, max_frame_delay, img):
        return HeroAnimation(max_frame, max_frame_delay, img)
        
    def is_alive(self):
        """Return true if player is alive"""
        return self.life > 0
    
    def lose_life(self):
        self.life = self.life - 1
