import pygame
import os.path
import configparser
import Map
import Enemy


class Game:
    def __init__(self):
        pygame.init()
        config = self.get_config()
        self.HEIGHT = int(config['window']['HEIGHT'])
        self.WIDTH = int(config['window']['WIDTH'])
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('TEDE')
        self.board = Map.Map()
        self.current_level = 0
        self.przeciwnik = Enemy.Enemy()

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
            clock = pygame.time.Clock()
            clock.tick(5)
            self.window.fill((0, 0, 0))
            self.board.draw_map(self.window, self.current_level)
            self.przeciwnik.sprite.draw(self.window)
            self.przeciwnik.make_move(self.przeciwnik.sprite.origin[0], self.przeciwnik.sprite.origin[1])
            self.przeciwnik.set_direction(self.board.get_map())
            # print(self.przeciwnik.sprite.origin)
            # print(self.przeciwnik.sprite.position)
            pygame.display.flip()
            self.check_events()
        pygame.quit()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
