#-*- coding: utf-8 -*-

from lib.base_entity import BaseEntity
from lib.base_animation import BaseAnimation
from pygame.locals import K_UP as UP

class MissileAnimation(BaseAnimation):
    """Custom class Animation : MissileAnimation

    """
    WIDTH_SPRITE_V = 17
    HEIGHT_SPRITE_V = 43

    WIDTH_SPRITE_H = 43
    HEIGHT_SPRITE_H = 17

    def get_sprite(self, move_direction):
        direction_num = move_direction - UP 
        if direction_num == 0 or direction_num == 1:            
            frame =  self.subsurface(
                self.WIDTH_SPRITE_V * self.frame,
                self.HEIGHT_SPRITE_V * direction_num,
                self.WIDTH_SPRITE_V,
                self.HEIGHT_SPRITE_V
            ).convert_alpha()
        else:
            direction_num = direction_num - 2
            frame = self.subsurface(
                0,
                self.HEIGHT_SPRITE_V * 2 + self.HEIGHT_SPRITE_H * (3 * direction_num + self.frame),
                self.WIDTH_SPRITE_H,
                self.HEIGHT_SPRITE_H
            ).convert_alpha()
        return frame
        
class Missile(BaseEntity):
    """Custom class Entity : Missile
    
    Entity for the missile. Represents missile
    and missile's animation
    """
    def __init__(self, typeof, rect_data):
        super(Missile, self).__init__(
            name='Missile%s' % str(typeof), 
            rect_data=rect_data, 
            speed=[3,3], 
            max_frame=3, 
            max_frame_delay=0, 
            img='img/Missile.png'
        )
        self.set_type(typeof)

    def direction_set(self, direction):
        self.direction = direction

    def init_animation(self, max_frame, max_frame_delay, img):
        return MissileAnimation(max_frame, max_frame_delay, img)
        
    def update(self, movement=None):
        """Custom Update function
        
        Update animation frame
        """
        self.move(self.direction)
        self.animation.update()
        self.setup_animation(self.direction)
    
    def set_type(self, typeof=0):
        """Create custom properties, linked with typeof.

        Typeof :
        - 0 : Normal
        - 1 : Fast
        - 2 : Very Fast
        """
        if typeof == 0:
            return
        if typeof == 1:
            self.speed = [
                self.speed[0]*2,
                self.speed[1]*2
            ]
        if typeof == 2:
            self.speed = [
                self.speed[0]*3,
                self.speed[1]*3
            ]
        
