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
            frame =  self.subsurface(
                0,
                self.frame * self.HEIGHT_SPRITE,
                self.WIDTH_SPRITE, 
                self.HEIGHT_SPRITE
            ).convert_alpha()
        else:
            frame =  self.subsurface(
                self.frame * self.HEIGHT_SPRITE,
                2 * self.HEIGHT_SPRITE,                
                self.HEIGHT_SPRITE,
                self.WIDTH_SPRITE, 
            ).convert_alpha()
        
        return frame
        
class Barrier(BaseEntity):
    """Custom class Entity : Barrier
    
    Entity for barrier. Represents barrier
    and barrier's animation
    """
    def __init__(self, rect_data):
        super(Barrier, self).__init__(
            name='Barrier',
            rect_data=rect_data,
            speed=[2,2],
            max_frame=2, 
            max_frame_delay=0, 
            img='img/Barriere.png'
        )
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
