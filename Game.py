import pygame
import os.path
import configparser
import Level0


class Game:
    def __init__(self):
        pygame.init()
        config = self.get_config()
        self.HEIGHT = int(config['window']['HEIGHT'])
        self.WIDTH = int(config['window']['WIDTH'])
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('TEDE')
        self.levels = [Level0.Level0()]
        self.current_level = 0

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

    def run(self):
        self.running = True
        while self.running:
            self.window.fill((0, 0, 0))
            self.levels[self.current_level].update(self.window)
            pygame.display.flip()
            self.check_events()
        pygame.quit()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
