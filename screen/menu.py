#-*- coding: utf-8 -*-

import pygame.key

from pygame.font import Font
from lib.base_screen import BaseScreen, ChangeScreenException
from pygame.locals import K_SPACE as SPACE

class MenuScreen(BaseScreen):

    def init_entities_before(self, surface):
        self.font = Font(None, 30)
        self.textImg = self.font.render('Press SPACE to BEGIN !',1,(255,255,255))
        surface.blit(self.textImg, (250,200))

    def execute(self, surface):
        if pygame.key.get_pressed()[SPACE] == 1:
            raise ChangeScreenException(1, 'Launch the game!')

    def draw(self, surface):
        pass
