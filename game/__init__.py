import pygame
import sys
from mainmenu import MenuClass
from settings import Settings
from gameLoop import GameLoop
from player import Player
from gameLoop.map import Map
from resolutions import Resolution
from controls import Controls
from util import load_save, reset_keys, write_save
from pygame import mixer


class GameStates:
    def __init__(self) -> None:
        self.gameState = "menu"
        self.gameStateList = ["menu", "game", "resolution",
                              "pause", "settings", "controls", "credits", "exit"]

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
monitor_size = [pygame.display.Info().current_w,
                pygame.display.Info().current_h]

size_x = monitor_size[0]*2/3
size_y = monitor_size[1]*2/3
screen = pygame.display.set_mode((size_x, size_y), pygame.RESIZABLE)
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
save = load_save()
gameStates = GameStates()
menu = MenuClass(size_x, size_y, screen, gameStates)
settings = Settings(size_x, size_y, screen, gameStates)
resolution = Resolution(size_x, size_y, screen, gameStates)
if gameStates.getState() != "game":
    mixer.music.load("game/assets/sounds/jiglr - Odyssey.mp3")
    mixer.music.play(-1)
    mixer.music.set_volume(1)
else:
    mixer.music.stop
while gameStates.getState() != "exit":
    while gameStates.getState() == "menu":
        # Path: game\mainmenu.py
        # This is where the menu code will go
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameStates.setState("exit")
            elif event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_SPACE:
                #     gameStates.setState("game")
                pass
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
                settings.settingsLoop(event, pygame.mouse.get_pos())
        clock.tick(60)
        # pygame.display.update()
    while gameStates.getState() == "resolution":
        # Path: game\settings.py
        # This is where the settings code will go
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameStates.setState("exit")
            else:
                resolution.resolutionsLoop(event, pygame.mouse.get_pos())
        clock.tick(60)

    if gameStates.getState() == "game":
        map = Map("game\\assets\\maps\\map4.mp",
                  "game\\assets\\Tiles\\tilemap.png")
        player = Player(screen, "game\\assets\\player\\player.png", map, {
                        "Left": 97, "Right": 100, "Jump": 119, "Dash": 32, "Stop": 27})
        mixer.music.stop()
        while gameStates.getState() == "game":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameStates.setState("exit")
                player.handleEvent(event)
            screen.fill((0, 0, 0))
            mapImg = player.map.getMap()
            screen.blit(mapImg, (player.mapX, player.mapY))
            player.update()
            pygame.display.update()
            clock.tick(60)


pygame.quit()
sys.exit()
