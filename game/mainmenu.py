import pygame
import sys
from button import Button


class MenuClass:
    def __init__(self, size_x: int, size_y: int, SCREEN) -> None:
        """create menu class"""
        self.MENU_MOUSE_POS = pygame.mouse.get_pos()
        self.size_x = size_x
        self.size_y = size_y
        self.SCREEN = SCREEN

        pygame.display.set_caption("Ba(TT)ery")
        self.BG = pygame.image.load("assets/")
        self.button_image = pygame.image.load("assets/")
        self.resize()

    def resize(self):
        """resize all images"""
        self.size_x, self.size_y = self.SCREEN.get_size()
        self.font_size_menu = self.size_y/10
        self.font_size_buttons = self.size_y/12
        self.BG = pygame.transform.scale(self.BG, (self.size_x, self.size_y))
        self.button_image = pygame.transform.scale(
            self.button_image, (self.size_x/4, self.size_y/10))

        self.PLAY_BUTTON = Button(self.button_image, pos=(self.size_x*1/6, self.size_y*2/3),
                                  text_input="PLAY", font=get_font(self.font_size_buttons), base_color="#d7fcd4", hovering_color="White")
        self.OPTIONS_BUTTON = Button(self.button_image, pos=(self.size_x/2, self.size_y*2/3),
                                     text_input="OPTIONS", font=get_font(self.font_size_buttons), base_color="#d7fcd4", hovering_color="White")
        self.QUIT_BUTTON = Button(self.button_image, pos=(self.size_x*5/6, self.size_y*2/3),
                                  text_input="QUIT", font=get_font(self.font_size_buttons), base_color="#d7fcd4", hovering_color="White")

        self.SCREEN.blit(self.BG, (0, 0))

        self.OPTIONS_BUTTON.update(self.SCREEN)
        self.PLAY_BUTTON.update(self.SCREEN)
        self.QUIT_BUTTON.update(self.SCREEN)

    def update(self):
        """update menu"""
        self.MENU_MOUSE_POS = pygame.mouse.get_pos()
        self.PLAY_BUTTON.changeColor(self.MENU_MOUSE_POS)
        self.OPTIONS_BUTTON.changeColor(self.MENU_MOUSE_POS)
        self.QUIT_BUTTON.changeColor(self.MENU_MOUSE_POS)
        self.resize()
        self.PLAY_BUTTON.update(self.SCREEN)
        self.OPTIONS_BUTTON.update(self.SCREEN)
        self.QUIT_BUTTON.update(self.SCREEN)
        pygame.display.update()
        pass

    def menuLoop(self, event):
        """ odpowiada za klikanie """
        self.MENU_MOUSE_POS = pygame.mouse.get_pos()
        # highlighting buttons
        for button in [self.PLAY_BUTTON, self.OPTIONS_BUTTON, self.QUIT_BUTTON]:
            button.changeColor(self.MENU_MOUSE_POS)
            button.update(self.SCREEN)

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.OPTIONS_BUTTON.checkForInput(self.MENU_MOUSE_POS)

            self.QUIT_BUTTON.checkForInput(self.MENU_MOUSE_POS)


def get_font(size: int):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", int(size))


if __name__ == '__main__':

    pygame.init()
    monitor_size = [pygame.display.Info().current_w,
                    pygame.display.Info().current_h]

    size_x = monitor_size[0]*2/3
    size_y = monitor_size[1]*2/3

    SCREEN = pygame.display.set_mode((size_x, size_y), pygame.RESIZABLE)


menu = MenuClass(size_x, size_y, SCREEN)
while True:

    MENU_MOUSE_POS = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            menu.resize()
        else:
            menu.menuLoop(event)

    pygame.display.update()
