import pygame
import os.path

pygame.init()


class Game:
    red = (255, 0, 0)

    # w sumie to nie wiem czy to tu
    def text_render(self, window, text_to_render, destination=(100, 100), color=red, size=20):
        my_font = pygame.font.SysFont('Comic Sans MS', size)
        rendered = my_font.render(text_to_render, 0, color)
        window.blit(rendered, destination)

    def check_files(self, file_name_list, window):
        errors = [file for file in file_name_list if os.path.isfile('images/' + file)]
        Game.text_render(window, errors)

