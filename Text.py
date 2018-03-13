import pygame

pygame.init()


class Text:
    red = (255, 0, 0)

    def __init__(self, string, position, color=red, font_size=30):
        self.text = str(string)
        self.color = color
        self.position = position
        self.font_size = font_size

    def text_render(self):
        my_font = pygame.font.SysFont('Comic Sans MS', self.font_size)
        rendered = my_font.render(self.text, 0, self.color)
        return rendered

