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
        if duration % 2 == 0 and duration != 0:
            self.start_time = time.time()
            return self.create_missile()
        return None

    def create_missile(self):
        random_int = random.randint(0,3)
        if random_int < 2:
            if random_int == 0:
                direction = self.south
                move_to = UP
            else:
                direction = self.north
                move_to = DOWN
            position = (
                random.randint(260,370),
                direction,
                15,
                40
            )
        else:
            if random_int == 2:
                direction = self.ouest
                move_to = RIGHT
            else:
                direction = self.east
                move_to = LEFT
            position = (
                direction,
                random.randint(180,280),
                40,
                15
            )
        missile = Missile(
            2,
            position,
        )
        missile.direction_set(move_to)
        return missile
    
    def level_up(self):
        if self.level < self.max_level:
            self.level = self.level + 1
