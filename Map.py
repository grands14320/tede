import Tile_manager
import pygame
import Game


class Map:
    def __init__(self):
        self.map = self.get_map()
        self.block = Tile_manager.TileManager()
        print(self.map)

    def get_map(self):
        map_list = []
        with open('mapa.txt', 'r') as file:
            for line in file.readlines():
                line = line.strip('\n')
                map_list.append(line.split("  "))
        return map_list

    def draw_map(self, window):
        for i in range(len(self.map)):
            for j in range(len(self.map)):
                self.block.get_tile(int(self.map[i][j]))
                window.blit(self.block, (i, j))

