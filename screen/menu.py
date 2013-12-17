#-*- coding: utf-8 -*-

from pygame.font import Font
from lib.base_screen import BaseScreen, ChangeScreenException

class MenuScreen(BaseScreen):

    def init_entities_before(self, surface):
        self.font = Font(None, 30)
        self.textImg = self.font.render('Press SPACE to BEGIN !',1,(255,255,255))
        surface.blit(self.textImg, (300,200))

    def execute(self, surface):
        pass

    def draw(self, surface):
        pass
