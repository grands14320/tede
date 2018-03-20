import pygame

pygame.init()


class Text:

    def __init__(self, string, position, color=(255, 0, 0), font_size=30):
        self.text = str(string)
        self.color = color
        self.position = position
        self.font_size = font_size

    def draw(self, window):
        my_font = pygame.font.SysFont('Comic Sans MS', self.font_size)
        window.blit(my_font.render(self.text, 0, self.color), self.position)

