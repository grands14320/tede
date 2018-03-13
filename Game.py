import pygame
import os.path
import configparser

pygame.init()

config_file_path = 'config.ini'
config = configparser.ConfigParser()
config.read(config_file_path)

WIDTH = config['window']['width']
HEIGHT = config['window']['height']


class Game:
    red = (255, 0, 0)
    config = configparser.ConfigParser()

    # w sumie to nie wiem czy to tu
    def text_render(self, window, text_to_render, destination=(100, 100), color=red, size=20):
        my_font = pygame.font.SysFont('Comic Sans MS', size)
        rendered = my_font.render(text_to_render, 0, color)
        window.blit(rendered, destination)

    def check_files(self, file_name_list, window):
        errors = [file for file in file_name_list if os.path.isfile('images/' + file)]
        Game.text_render(window, errors)



