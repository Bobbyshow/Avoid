#-*- coding: utf-8 -*-

from lib.base_entity import BaseEntity
from lib.base_animation import BaseAnimation
from pygame.locals import K_UP as UP


class BarrierAnimation(BaseAnimation):
    """Custom class Animation : BarrierAnimation

    """
    WIDTH_SPRITE = 121 
    HEIGHT_SPRITE = 28
    
    def get_sprite(self, move_direction):
        if move_direction - UP == 0 or move_direction - UP == 1:
            direction_num = 0
        else:
            direction_num = 1
        frame =  self.subsurface(
            direction_num * self.WIDTH_SPRITE,
            self.frame * self.HEIGHT_SPRITE,
            self.WIDTH_SPRITE, 
            self.HEIGHT_SPRITE
        ).convert_alpha()
        return frame
        
class Barrier(BaseEntity):
    """Custom class Entity : Barrier
    
    Entity for barrier. Represents barrier
    and barrier's animation
    """
    def direction_set(self, direction):
        self.direction = direction

    def init_animation(self, max_frame, max_frame_delay, img):
        return BarrierAnimation(max_frame, max_frame_delay, img)
        
    def update(self, movement = None):
        """Custom Update function
        
        update animation frame
        """
        self.animation.update()
        self.setup_animation(self.direction)
