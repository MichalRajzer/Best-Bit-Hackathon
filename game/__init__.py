import pygame
import sys
from mainmenu import MenuClass
from settings import Settings


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


# Path: game\__init__.py
pygame.init()
pygame.display.set_caption("My Game")
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
clock = pygame.time.Clock()
gameStates = GameStates()
menu = MenuClass(800, 600, screen, gameStates)
settings = Settings(800, 600, screen, gameStates)
while gameStates.getState() != "exit":
    while gameStates.getState() == "menu":
        # Path: game\mainmenu.py
        # This is where the menu code will go
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameStates.setState("exit")
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    inMenu = False
                    inGame = True
            else:
                menu.menuLoop(event, pygame.mouse.get_pos())
        clock.tick(60)
        # pygame.display.update()
    while gameStates.getState() == "settings":
        # Path: game\settings.py
        # This is where the settings code will go
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameStates.setState("exit")
            else:
                settings .settingsLoop(event, pygame.mouse.get_pos())
        clock.tick(60)
        # pygame.display.update()
    while gameStates.getState() == "inGame":
        pass

pygame.quit()
sys.exit()
