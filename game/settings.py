import pygame, os 
from button import Button, volume_button


class Settings:
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
        self.arrow_up = pygame.image.load(os.path.join(self.dirname, "assets/arrow_up.png"))
        self.button_music = pygame.image.load(os.path.join(self.dirname, "assets/button_music.png"))
        self.arrow_down = pygame.image.load(os.path.join(self.dirname, "assets/arrow_down.png"))
        background = os.path.join(self.dirname, 'assets/bg.png')
        self.BG = pygame.image.load(background)
        button = os.path.join(self.dirname, 'assets/menu_button.png')
        self.button_image = pygame.image.load(button)
        self.arrow_up = pygame.transform.scale(self.arrow_up, (self.size_x//10, self.size_y//10))
        self.arrow_down = pygame.transform.scale(self.arrow_down, (self.size_x//10, self.size_y//10))

        self.resize()
        
    def resize(self):
        """resize all images"""
        self.size_x, self.size_y = self.SCREEN.get_size()
        self.font_size_menu = self.size_y*1/22
        self.font_size_buttons = self.size_y/16
        self.button_music = pygame.transform.scale(self.button_music, (int(self.size_x/5), int(self.size_y/5)))
        self.BG = pygame.transform.scale(self.BG, (self.size_x, self.size_y))
        self.button_image = pygame.transform.scale(
            self.button_image, (self.size_x*3/10, self.size_y*3/20))
        self.button_image_res = pygame.transform.scale(
            self.button_image, (self.size_x*4/10, self.size_y*3/20))
        f = open('game//volume.txt','r')
        volum = f.read()
        f.close()
        volum = float(volum)
        volum = int(volum*10)
        self.VOLUME = str(volum )
        self.VOLUME_BUTTON = volume_button(self.SCREEN, pos=(self.size_x/2, self.size_y*5/8), text_input="VOLUME", image=self.button_image, font=get_font(self.font_size_menu),base_color="#d7fcd4", value=0)
        self.MONITOR_VOLUME = volume_button(self.SCREEN,pos=(self.size_x*3/4, self.size_y*15/24), image=self.button_music,text_input= self.VOLUME,base_color="#d7fcd4",font=get_font(self.font_size_menu), value= 0)
        self.VOLUME_UP = volume_button(self.SCREEN, pos=(self.size_x*3/4, self.size_y*6/12),image = self.arrow_up, text_input= ' ',base_color="#d7fcd4", font=get_font(self.font_size_menu), value= "UP")
        self.VOLUME_DOWN = volume_button(self.SCREEN, pos=(self.size_x*3/4, self.size_y*9/12),image = self.arrow_down, text_input= ' ',base_color="#d7fcd4", font=get_font(self.font_size_menu), value= "DOWN")            
        self.RESOLUTION_BUTTON = Button(self.button_image_res, pos=(self.size_x/2, self.size_y*9/24),
                                     text_input="RESOLUTIONS", font=get_font(self.font_size_menu), base_color="#d7fcd4", hovering_color="White", gamestates=self.gamestates, type="resolution")
        self.BACK_BUTTON = Button(self.button_image, pos=(self.size_x/2, self.size_y*5/6),
                                  text_input="BACK", font=get_font(self.font_size_buttons), base_color="#d7fcd4", hovering_color="White", gamestates=self.gamestates, type="menu")

        self.SCREEN.blit(self.BG, (0, 0))
        self.MONITOR_VOLUME.update(self.SCREEN)
        self.VOLUME_BUTTON.update(self.SCREEN)
        self.VOLUME_DOWN.update(self.SCREEN)
        self.VOLUME_UP.update(self.SCREEN)
        self.RESOLUTION_BUTTON.update(self.SCREEN)
        self.BACK_BUTTON.update(self.SCREEN)

    def update(self):
        """ Update menu """
        self.MENU_MOUSE_POS = pygame.mouse.get_pos()
        self.MONITOR_VOLUME.changeColor(self.MENU_MOUSE_POS)
        self.VOLUME_UP.changeColor(self.MENU_MOUSE_POS)
        self.VOLUME_BUTTON.changeColor(self.MENU_MOUSE_POS)
        self.VOLUME_DOWN.changeColor(self.MENU_MOUSE_POS)
        self.RESOLUTION_BUTTON.changeColor(self.MENU_MOUSE_POS)
        self.BACK_BUTTON.changeColor(self.MENU_MOUSE_POS)
        self.resize()

    def settingsLoop(self, event, mouse_pos):
        """ Odpowiada za klikanie """
        self.update()
        self.MENU_MOUSE_POS = mouse_pos
        for button in [self.RESOLUTION_BUTTON, self.BACK_BUTTON]:
            button.changeColor(self.MENU_MOUSE_POS)
            button.update(self.SCREEN)

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.VOLUME_DOWN.checkForInput(self.MENU_MOUSE_POS)
            self.VOLUME_UP.checkForInput(self.MENU_MOUSE_POS)
            self.RESOLUTION_BUTTON.checkForInput(self.MENU_MOUSE_POS)
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
    settings = Settings(size_x, size_y, SCREEN, gamestates)
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
        
        
