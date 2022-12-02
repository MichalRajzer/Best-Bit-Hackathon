import pygame
import sys

if __name__ == "__main__":
    # Path: game\__init__.py
    pygame.init()
    pygame.display.set_caption("My Game")
    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    clock = pygame.time.Clock()
    running = True
    inMenu = True    # This is the variable that will be used to determine if the game is in the menu or not
    inGame = False   # This is the variable that will be used to determine if the game is in the game loop or not
    inPause = False  # This is the variable that will be used to determine if the game is in the pause menu or not
    while running:
        while inMenu:
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

            # Flip the display
    pygame.quit()
    sys.exit()
