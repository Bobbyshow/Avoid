#-*- coding: utf-8 -*-

import time
import random

from pygame.locals import K_LEFT as LEFT
from pygame.locals import K_DOWN as DOWN 
from pygame.locals import K_UP as UP
from pygame.locals import K_RIGHT as RIGHT

from missile import Missile

class MissileGenerator():
    """Class MissileGenerator.
        
    Can generate missiles on map.
    """
    north = -20
    east = 660
    south = 500
    ouest = -20
    
    def __init__(self):
        self.start_time = time.time()
        self.level = 1
        self.max_level = 5

    def check_generation(self):
        duration = int(time.time() - self.start_time)
        if duration % 1 == 0 and duration != 0:
            self.start_time = time.time()
            return self.create_missile()
        return None

    def create_missile(self):
        if random.randint(0,3) == 0:
            position = (
                random.randint(260,370),
                self.south,
                15,
                40
            )
            missile = Missile(
                'Missile',
                position,
                [3,3],
                3,
                0,
                'img/Missile.png'
            )
            missile.direction_set(UP)
        elif random.randint(0,3) == 1:
            position = (
                random.randint(260,370),
                self.north,
                15,
                40
            )
            missile = Missile(
                'Missile',
                position,
                [3,3],
                3,
                0,
                'img/Missile.png'
            )
            missile.direction_set(DOWN)
        elif random.randint(0,3) == 2:
            position = (
                self.ouest,
                random.randint(180,280),
                40,
                15
            )
            missile = Missile(
                'Missile',
                position,
                [3,3],
                3,
                0,
                'img/Missile.png'
            )
            missile.direction_set(RIGHT)
        elif random.randint(0,3) == 3:
            position = (
                self.east,
                random.randint(180,280),
                40,
                15
            )
            missile = Missile(
                'Missile',
                position,
                [3,3],
                3,
                0,
                'img/Missile.png'
            )
            missile.direction_set(LEFT)
        else:
            return None
        return missile
    
    def level_up(self):
        if self.level < self.max_level:
            self.level = self.level + 1
    
    
    
