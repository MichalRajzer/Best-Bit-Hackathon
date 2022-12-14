import pygame
import sys
from button import Button
from pygame import mixer
import os


class GameStates:
    def __init__(self) -> None:
        self.gameState = "menu"
        self.gameStateList = ["menu", "game",
                              "pause", "settings", "credits", "exit"]

    def getState(self):
        return self.gameState

    def setState(self, state):
        print("state changed to", state)
        if state in self.gameStateList:
            self.gameState = state
        else:
            raise ValueError("Invalid game state")


class MenuClass:
    def __init__(self, size_x: int, size_y: int, SCREEN, gamestates) -> None:
        """create menu class"""
        self.gamestates = gamestates
        self.MENU_MOUSE_POS = pygame.mouse.get_pos()
        self.size_x = size_x
        self.size_y = size_y
        self.SCREEN = SCREEN

        pygame.display.set_caption("Ba(TT)ery")
        self.dirname = os.path.dirname(__file__)
        background = os.path.join(self.dirname, 'assets/bg_logo.png')
        self.BG = pygame.image.load(background)
        button = os.path.join(self.dirname, 'assets/menu_button.png')
        self.button_image = pygame.image.load(button)

        self.resize()

    def resize(self):
        """resize all images"""
        self.size_x, self.size_y = self.SCREEN.get_size()
        self.font_size_menu = self.size_y/10
        self.font_size_buttons = self.size_y/16
        self.BG = pygame.transform.scale(self.BG, (self.size_x, self.size_y))
        self.button_image = pygame.transform.scale(
            self.button_image, (self.size_x*3/10, self.size_y*3/20))

        self.PLAY_BUTTON = Button(self.button_image, pos=(self.size_x*5/28, self.size_y*8/15),
                                  text_input="PLAY", font=get_font(self.font_size_buttons), base_color="#d7fcd4", hovering_color="White", gamestates=self.gamestates, type="game")
        self.OPTIONS_BUTTON = Button(self.button_image, pos=(self.size_x/2, self.size_y*8/15),
                                     text_input="OPTIONS", font=get_font(self.font_size_buttons), base_color="#d7fcd4", hovering_color="White", gamestates=self.gamestates, type="settings")
        self.QUIT_BUTTON = Button(self.button_image, pos=(self.size_x*23/28, self.size_y*8/15),
                                  text_input="QUIT", font=get_font(self.font_size_buttons), base_color="#d7fcd4", hovering_color="White", gamestates=self.gamestates, type="exit")

        self.SCREEN.blit(self.BG, (0, 0))

        self.OPTIONS_BUTTON.update(self.SCREEN)
        self.PLAY_BUTTON.update(self.SCREEN)
        self.QUIT_BUTTON.update(self.SCREEN)

    def update(self):
        """ Update menu """
        self.MENU_MOUSE_POS = pygame.mouse.get_pos()
        self.PLAY_BUTTON.changeColor(self.MENU_MOUSE_POS)
        self.OPTIONS_BUTTON.changeColor(self.MENU_MOUSE_POS)
        self.QUIT_BUTTON.changeColor(self.MENU_MOUSE_POS)
        self.resize()

    def menuLoop(self, event, mouse_pos):
        """ Odpowiada za klikanie """
        self.update()
        self.MENU_MOUSE_POS = mouse_pos
        for button in [self.PLAY_BUTTON, self.OPTIONS_BUTTON, self.QUIT_BUTTON]:
            button.changeColor(self.MENU_MOUSE_POS)
            button.update(self.SCREEN)

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("click")
            self.PLAY_BUTTON.checkForInput(self.MENU_MOUSE_POS)
            self.OPTIONS_BUTTON.checkForInput(self.MENU_MOUSE_POS)
            self.QUIT_BUTTON.checkForInput(self.MENU_MOUSE_POS)
        elif event.type == pygame.VIDEORESIZE:
            self.resize()
        pygame.display.update()


def get_font(size: int):  # Returns Press-Start-2P in the desired size
    font = os.path.join(os.path.dirname(__file__), 'assets/fonts/font.ttf')
    return pygame.font.Font(font, int(size))


if __name__ == '__main__':
    state = GameStates()
    pygame.init()
    monitor_size = [pygame.display.Info().current_w,
                    pygame.display.Info().current_h]

    size_x = monitor_size[0]*2/3
    size_y = monitor_size[1]*2/3

    SCREEN = pygame.display.set_mode((size_x, size_y), pygame.RESIZABLE)

    menu = MenuClass(size_x, size_y, SCREEN, state)
    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            else:
                menu.menuLoop(event, MENU_MOUSE_POS)

        # pygame.display.update()
