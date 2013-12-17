#-*- coding: utf-8 -*-

import random

from lib.base_entity import BaseEntity
from lib.base_animation import BaseAnimation


class LifeAnimation(BaseAnimation):
    """Custom class : Life Animation."""
    WIDTH_SPRITE = 16 
    HEIGHT_SPRITE = 17
    
    def get_sprite(self, move_direction):
        frame = self.subsurface(
            0,
            self.frame * self.HEIGHT_SPRITE,
            self.WIDTH_SPRITE, 
            self.HEIGHT_SPRITE
        ).convert_alpha()
        return frame
    
    def update(self):
        """ Custom animation update.

        Random change for frame 1->2
        Fix change for frame 2->1
        """
        if self.frame == 0:
            if random.random()*100 > 99:
                self.frame = (self.frame + 1) % self.max_frame   
                self.frame_delay = self.max_frame_delay
        else:
            if self.frame_delay < 0:
                self.frame = (self.frame + 1) % self.max_frame   
                self.frame_delay = self.max_frame_delay
            else:
                self.frame_delay = self.frame_delay - 1
    
 
class Life(BaseEntity):
    """Custom class: Life entity."""
    def __init__(self, name, rect_data, speed, max_frame, max_frame_delay, img):
        super(Life, self).__init__(name, rect_data, speed, max_frame, max_frame_delay, img)

    def init_animation(self, max_frame, max_frame_delay, img):
        return LifeAnimation(max_frame, max_frame_delay, img)
    
    def update(self, movement = None):
        """Custom Update function
        
        update animation frame
        """        
        self.animation.update()
        self.setup_animation(self.direction)
