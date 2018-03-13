import pygame
import os.path
import configparser
from Text import Text
pygame.init()


class Game:
    def __init__(self):
        self.HEIGHT = self.get_config()['window']['HEIGHT']
        self.WIDTH = self.get_config()['window']['WIDTH']
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

    @staticmethod
    def touch(path, data=''):
        with open(path, 'a+') as file:
            file.write(data)

    def check_files(self, file_name_list):
        return [file for file in file_name_list if not os.path.isfile('images/' + file)]

    def get_config(self, config_file_path='config.ini'):
        config = """
        [window] \n
        width=600 \n
        height=800 \n
        fps = 30 \n   
        """
        if not os.path.exists(config_file_path):
            Game.touch(os.getcwd(), config)
        config = configparser.ConfigParser()
        config.read(config_file_path)
        return config


