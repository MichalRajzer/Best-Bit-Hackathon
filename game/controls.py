import pygame
import os
from button import Button
from util import write_save


class Controls:
    def __init__(self, size_x: int, size_y: int, SCREEN, gamestates, save) -> None:
        """create settings class"""
        self.save_file = save
        self.curr_block = save["current_profile"]
        self.controls = self.save_file["controls"][str(self.curr_block)]
        self.gamestates = gamestates
        self.MENU_MOUSE_POS = pygame.mouse.get_pos()
        self.size_x = size_x
        self.size_y = size_y
        self.SCREEN = SCREEN
        self.gamestate = gamestates

        pygame.display.set_caption("Ba(TT)ery")
        self.dirname = os.path.dirname(__file__)
        background = os.path.join(self.dirname, 'assets/bg.png')
        self.BG = pygame.image.load(background)
        button = os.path.join(self.dirname, 'assets/menu_button.png')
        self.button_image = pygame.image.load(button)

        self.resize()
        self.setup()

    def setup(self):
        """ Setup menu """
        self.selected = False
        self.cursor_dict = {}
        self.font = get_font(self.font_size_buttons)
        self.curr_index = 0
        i = 0
        for control in self.controls:
            self.cursor_dict[i] = control
            i += 1
        self.cursor_dict[i] = "Set"
    


    def resize(self):
        """resize all images"""
        self.size_x, self.size_y = self.SCREEN.get_size()
        self.font_size_menu = self.size_y/10
        self.font_size_buttons = self.size_y/16
        self.BG = pygame.transform.scale(self.BG, (self.size_x, self.size_y))
        self.button_image = pygame.transform.scale(
            self.button_image, (self.size_x*3/10, self.size_y*3/20))

        
        self.BACK_BUTTON = Button(self.button_image, pos=(self.size_x/2, self.size_y*5/6),
                                  text_input="BACK", font=get_font(self.font_size_buttons), base_color="#d7fcd4", hovering_color="White", gamestates=self.gamestates, type="settings")

        self.SCREEN.blit(self.BG, (0, 0))
        self.BACK_BUTTON.update(self.SCREEN)

    def update(self):
        """ Update menu """
        self.MENU_MOUSE_POS = pygame.mouse.get_pos()
        self.BACK_BUTTON.changeColor(self.MENU_MOUSE_POS)
        self.resize()

    def controlsLoop(self, event, mouse_pos):
        """ Odpowiada za klikanie """
        self.update()
        self.MENU_MOUSE_POS = mouse_pos
        for button in [self.BACK_BUTTON]:
            button.changeColor(self.MENU_MOUSE_POS)
            button.update(self.SCREEN)

        if event.type == pygame.MOUSEBUTTONDOWN:
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
    monitor_size = [pygame.display.Info().current_w,
                    pygame.display.Info().current_h]

    size_x = monitor_size[0]*2/3
    size_y = monitor_size[1]*2/3

    SCREEN = pygame.display.set_mode((size_x, size_y), pygame.RESIZABLE)
    gamestates = {"game": False, "settings": False, "exit": False}
    settings = Controls(size_x, size_y, SCREEN, gamestates)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            settings.controlsLoop(event, pygame.mouse.get_pos())
            if gamestates["game"]:
                print("game")
            elif gamestates["settings"]:
                print("settings")
            elif gamestates["exit"]:
                print("exit")
                pygame.quit()
