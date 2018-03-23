import pygame
import os.path
import configparser
pygame.init()


class Game:
    def __init__(self):
        config = self.get_config()
        self.HEIGHT = config['window']['HEIGHT']
        self.WIDTH = config['window']['WIDTH']
        # (self.WIDTH, self.HEIGHT)
        self.window = pygame.display.set_mode((800,600))
        pygame.display.set_caption('TEDE')
        self.game_loop()

    def create_config_file(self, path):

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
            self.create_config_file(os.getcwd())
        config = configparser.ConfigParser()
        config.read(config_file_path)
        return config

    def game_loop(self):
        self.running = True
        while self.running:
            self.check_events()
        pygame.quit()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

game1 = Game()
