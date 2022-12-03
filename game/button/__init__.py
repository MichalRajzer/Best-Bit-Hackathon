import pygame
from pygame import mixer


class Button:
    def __init__(self, image, pos, text_input, font, base_color, hovering_color, gamestates, type):
        self.image = image
        self.type = type
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.text_input = text_input
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        self.gamestates = gamestates

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position, isRes=False):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.onClick(isRes=isRes)
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(
                self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(
                self.text_input, True, self.base_color)

    def onClick(self, isRes=False):
        mixer.Sound("game\\assets\\sounds\\button.wav").play()
        if isRes == False:
            self.gamestates.setState(self.type)
        else:
            pygame.display.set_mode(isRes)
