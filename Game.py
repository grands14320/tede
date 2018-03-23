import pygame
import os.path
import configparser
import map
from map import Map
pygame.init()


class Game:
    def __init__(self):
        self.HEIGHT = self.get_config()['window']['HEIGHT']
        self.WIDTH = self.get_config()['window']['WIDTH']
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.map = map.Map

    def create_config_file(path):
        
        config = """
            [window] \n
            width=600 \n
            height=800 \n
            fps = 30 \n   
            """
        
        with open(path, 'a+') as file:
            file.write(config)

    def check_files(self, file_name_list):
        return [file for file in file_name_list if not os.path.isfile('images/' + file)]

    def get_config(self, config_file_path='config.ini'):
        if not os.path.exists(config_file_path):
            create_config_file(os.getcwd())
       
        config = configparser.ConfigParser()
        config.read(config_file_path)
        return config



