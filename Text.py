import pygame

pygame.init()


class Text:
    red = (255, 0, 0)

    @staticmethod
    def text_render(window, text_to_render, destination=(100, 100), color=red, size=20):
        my_font = pygame.font.SysFont('Comic Sans MS', size)
        rendered = my_font.render(text_to_render, 0, color)
        window.blit(rendered, destination)
