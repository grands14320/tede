import Tile_manager


class Map:
    def __init__(self):
        self.map = self.get_map()
        self.block = Tile_manager.TileManager()

    def get_map(self):
        map_list = []
        with open('mapa.txt', 'r') as file:
            for line in file.readlines():
                line = line.strip('\n')
                map_list.append([line])
        return map_list

    def draw_map(self):
        for i in range(len(self.map)):
            for j in range(len(self.map)):
                self.block.get_tile(self.map[i][j])

