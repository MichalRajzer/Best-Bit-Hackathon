import pygame
import sys
from mainmenu import MenuClass


class GameStates:
    def __init__(self) -> None:
        self.gameState = "menu"
        self.gameStateList = ["menu", "game",
                              "pause", "settings", "credits", "exit"]

    def getState(self):
        return self.gameState

    def setState(self, state):
        if state in self.gameStateList:
            self.gameState = state
        else:
            raise ValueError("Invalid game state")

class Settings:
    def __init__(self) -> None:
        self.settings = {
            "fullscreen": False,
            "resolution": [800, 600],
            "volume": 0.5,
            "fps": 60,
            "vsync": True,
        }
        self.def_settings = {
            "fullscreen": False,
            "resolution": [1280, 720],
            "volume": 0.5,
            "fps": 60,
            "vsync": True,
        }

    def getdef_settings(self):
        return self.def_settings

    def getSettings(self):
        return self.settings

    def setSettings(self, settings):
        self.settings = settings


# Path: game\__init__.py
pygame.init()
pygame.display.set_caption("My Game")
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
clock = pygame.time.Clock()
gameStates = GameStates()
menu = MenuClass(800, 600, screen, gameStates)
while gameStates.getState() != "exit":
    while gameStates.getState() == "menu":
        # Path: game\mainmenu.py
        # This is where the menu code will go
        for event in pygame.event.get():
            menu.menuLoop(event)
            if event.type == pygame.QUIT:
                gameStates.setState("exit")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    inMenu = False
                    inGame = True
        clock.tick(60)
    while inGame:
        pass

pygame.quit()
sys.exit()
