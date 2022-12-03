import pygame
import os
from button import Button


class Resolution:
    def __init__(self, size_x: int, size_y: int, SCREEN, gamestates) -> None:
        """create settings class"""
        self.gamestates = gamestates
        self.MENU_MOUSE_POS = pygame.mouse.get_pos()
        self.size_x = size_x
        self.size_y = size_y
        self.SCREEN = SCREEN
        self.gamestate = gamestates

        pygame.display.set_caption("Ba(TT)ery")
        self.dirname = os.path.dirname(__file__)
        background = os.path.join(self.dirname, 'assets/background.png')
        self.BG = pygame.image.load(background)
        button = os.path.join(self.dirname, 'assets/menu_button.png')
        self.button_image = pygame.image.load(button)

        self.resize()

    def resize(self):
        """resize all images"""
        self.size_x, self.size_y = self.SCREEN.get_size()
        self.font_size_menu = self.size_y/10
        self.font_size_buttons = self.size_y/20
        self.BG = pygame.transform.scale(self.BG, (self.size_x, self.size_y))
        self.button_image = pygame.transform.scale(
            self.button_image, (self.size_x/4, self.size_y/10))
        self.RES_1920_1080_BUTTON = Button(None, pos=(self.size_x/2, self.size_y*1/6),
                                  text_input="1920x1080", font=get_font(self.font_size_buttons), base_color="#d7fcd4", hovering_color="White", gamestates=self.gamestates, type="settings")        
        self.RES_1080_720_BUTTON = Button(None, pos=(self.size_x/2, self.size_y*2/6),
                                  text_input="1080x720", font=get_font(self.font_size_buttons), base_color="#d7fcd4", hovering_color="White", gamestates=self.gamestates, type="settings")
        self.RES_800_600_BUTTON = Button(None, pos=(self.size_x/2, self.size_y*3/6),
                                  text_input="800x600", font=get_font(self.font_size_buttons), base_color="#d7fcd4", hovering_color="White", gamestates=self.gamestates, type="settings")
        self.BACK_BUTTON = Button(self.button_image, pos=(self.size_x/2, self.size_y*5/6),
                                  text_input="BACK", font=get_font(self.font_size_buttons), base_color="#d7fcd4", hovering_color="White", gamestates=self.gamestates, type="settings")

        self.SCREEN.blit(self.BG, (0, 0))
        self.RES_1920_1080_BUTTON.update(self.SCREEN)
        self.RES_1080_720_BUTTON.update(self.SCREEN)
        self.RES_800_600_BUTTON.update(self.SCREEN)
        self.BACK_BUTTON.update(self.SCREEN)

    def update(self):
        """ Update menu """
        self.MENU_MOUSE_POS = pygame.mouse.get_pos()
        self.RES_1920_1080_BUTTON.changeColor(self.MENU_MOUSE_POS)
        self.RES_1080_720_BUTTON.changeColor(self.MENU_MOUSE_POS)
        self.RES_800_600_BUTTON.changeColor(self.MENU_MOUSE_POS)
        self.BACK_BUTTON.changeColor(self.MENU_MOUSE_POS)
        self.resize()

    def settingsLoop(self, event, mouse_pos):
        """ Odpowiada za klikanie """
        self.update()
        self.MENU_MOUSE_POS = mouse_pos
        for button in [self.BACK_BUTTON, self.RES_800_600_BUTTON, self.RES_1080_720_BUTTON, self.RES_1920_1080_BUTTON]:
            button.changeColor(self.MENU_MOUSE_POS)
            button.update(self.SCREEN)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.RES_1920_1080_BUTTON.checkForInput(self.MENU_MOUSE_POS, isRes=(1920, 1080)):
                pass
            elif self.RES_1080_720_BUTTON.checkForInput(self.MENU_MOUSE_POS, isRes=(1080, 720)):
                pass
            elif self.RES_800_600_BUTTON.checkForInput(self.MENU_MOUSE_POS, isRes=(800, 600)):
                pass
            self.BACK_BUTTON.checkForInput(self.MENU_MOUSE_POS)
        elif event.type == pygame.VIDEORESIZE:
            self.resize()
        pygame.display.update()


def get_font(size: int):  # Returns Press-Start-2P in the desired size
    font = os.path.join(os.path.dirname(__file__), 'assets/fonts/font.ttf')
    return pygame.font.Font(font, int(size))


if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    SCREEN = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    gamestates = {"game": False, "settings": False, "exit": False}
    settings = Resolution(800, 600, SCREEN, gamestates)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            settings.settingsLoop(event, pygame.mouse.get_pos())
            if gamestates["game"]:
                print("game")
            elif gamestates["settings"]:
                print("settings")
            elif gamestates["exit"]:
                print("exit")
                pygame.quit()
