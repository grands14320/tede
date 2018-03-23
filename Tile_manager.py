import pygame
import Map,Sprite


class TileManager:

    def __init__(self):
        self.mapa1 = Map.Map


    def get_tile(self, index_x, index_y):
        if self.mapa1.map[index_x][index_y] == 1:
            return
        elif self.mapa1.map[index_x][index_y] == 2:
            return
        else:
            return

