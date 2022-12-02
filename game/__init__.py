import pygame
import sys


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


# Path: game\__init__.py
pygame.init()
pygame.display.set_caption("My Game")
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
clock = pygame.time.Clock()
gameStates = GameStates()
while gameStates.getState() != "exit":
    while gameStates.getState() == "menu":
        # Path: game\mainmenu.py
        # This is where the menu code will go
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    inMenu = False
                    running = False
                elif event.key == pygame.K_RETURN:
                    inMenu = False
                    running = False
                if event.key == pygame.K_SPACE:
                    inMenu = False
                    inGame = True
        screen.fill((70, 0, 70))
        pygame.display.flip()
        clock.tick(60)
    while inGame:
        pass

pygame.quit()
sys.exit()
