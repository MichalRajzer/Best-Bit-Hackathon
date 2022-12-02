import pygame
import sys
from button import Button


class MenuClass:
    def __init__(self, size_x:int, size_y:int, screen) -> None:        
        """create menu class"""
        self.MENU_MOUSE_POS = pygame.mouse.get_pos()
        self.size_x = size_x
        self.size_y = size_y
        self.screen = screen
        
        pygame.display.set_caption("Ba(TT)ery")

        pass

