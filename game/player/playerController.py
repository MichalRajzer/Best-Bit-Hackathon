import pygame


class PlayerController:
    def __init__(self, player, keyUp=pygame.K_w, keyDown=pygame.K_s, keyLeft=pygame.K_a, keyRight=pygame.K_d) -> None:
        """
        Basic player controller
        player to be the player object to be controlled"""
        self.keyUp = keyUp
        self.keyDown = keyDown
        self.keyLeft = keyLeft
        self.keyRight = keyRight
        self.player = player

    def update(self, events):
        """
        Update player position based on key presses
        events is a list of pygame events"""
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == self.keyUp:
                    self.move(0)
                elif event.key == self.keyDown:
                    self.move(1)
                elif event.key == self.keyLeft:
                    self.move(2)
                elif event.key == self.keyRight:
                    self.move(3)

    def move(self, direction):
        """Move player in a direction (0 = up, 1 = down, 2 = left, 3 = right)"""
        self.player.move()
