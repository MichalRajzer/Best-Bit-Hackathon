import pygame
import sys

if __name__ == "__main__":
    # Path: game\__init__.py
    pygame.init()
    pygame.display.set_caption("My Game")
    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    clock = pygame.time.Clock()
    running = True
    inMenu = True  # This is the variable that will be used to determine if the game is in the menu or not
    inGame = False  # This is the variable that will be used to determine if the game is in the game loop or not
    inPause = False  # This is the variable that will be used to determine if the game is in the pause menu or not
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((70, 0, 70))

        # Flip the display
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    sys.exit()
