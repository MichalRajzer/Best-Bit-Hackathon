import pygame
from pygame.locals import *
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
        self.BG = pygame.image.load("assets/")
        self.button_image = pygame.image.load("assets/")
        self.resize()

    def resize(self):
        """resize all images"""
        self.size_x, self.size_y = self.screen.get_size()
        self.font_size_menu = self.size_y/10
        self.font_size_buttons = self.size_y/12
        self.BG = pygame.transform.scale(self.BG, (self.size_x, self.size_y))
        self.button_image = pygame.transform.scale(self.button_image,(self.size_x/4, self.size_y/10))
        
        self.PLAY_BUTTON = Button(self.button_image, pos=(self.size_x*1/6, self.size_y*2/3), 
                            text_input="PLAY", font=get_font(self.font_size_buttons), base_color="#d7fcd4", hovering_color="White")
        self.OPTIONS_BUTTON = Button(self.option_button, pos=(self.size_x/2, self.size_y*2/3), 
                            text_input="OPTIONS", font=get_font(self.font_size_buttons), base_color="#d7fcd4", hovering_color="White")
        self.QUIT_BUTTON = Button(self.button_image, pos=(self.size_x*5/6, self.size_y*2/3), 
                            text_input="QUIT", font=get_font(self.font_size_buttons), base_color="#d7fcd4", hovering_color="White")

        self.screen.blit(self.BG, (0, 0))
        self.screen.blit(self.MENU_TEXT, self.MENU_RECT)

        self.OPTIONS_BUTTON.update(SCREEN)
        self.PLAY_BUTTON.update(SCREEN)
        self.QUIT_BUTTON.update(SCREEN)
        

    def update(self):




        pass

