#-*- coding: utf-8 -*-

import pygame.key

from pygame.font import Font
from lib.base_screen import BaseScreen, ChangeScreenException
from pygame.locals import K_SPACE as SPACE

class MenuScreen(BaseScreen):

    def init_entities_before(self, surface):
        self.font = Font(None, 30)
        self.textImg = self.font.render(
            'Press SPACE to BEGIN !',
            1,
            (255,255,255)
        )
        surface.blit(self.textImg, (250,200))

    def execute(self, surface):
        if pygame.key.get_pressed()[SPACE] == 1:
            raise ChangeScreenException(1, 'Launch the game!')

    def erase_all_map(self):
        pass

    def draw(self, surface):
        pass
    
    def game_over(self, text, number=None):
        BaseScreen.erase_all_map(self)
        font = Font(None, 30)
        textImg = font.render(text, 1 ,(255,255,255))
        self.surface.blit(textImg, (250,100))
        
