import pygame


class Map:
    def get_map(self):
        map = []
        with open('mapa.txt', 'r') as file:
            for line in file.readlines():
                line = line.strip('\n')
                map.append([line])
        return map

