import pygame


class Map:
    def __init__(self):
        self.map_array = self.get_map()

    def get_map(self):
        map = []
        with open('mapa.txt', 'r') as file:
            for line in file.readlines():
                line = line.strip('\n')
                map.append([line])
        return map

