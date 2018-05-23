import Sprite


class Level:
    def __init__(self):
        self.tiles = []

    def get_tile(self, point):
        return self.tiles[point-1].get_surface()

    def get_map(self):
        map_list = []
        with open('mapa.txt', 'r') as file:
            for line in file.readlines():
                line = line.strip('\n')
                map_list.append(line.split("  "))
        return map_list
