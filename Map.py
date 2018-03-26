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
                map_list.append(line.split("  "))
        return map_list

    def draw_map(self, window):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                window.blit(self.block.get_tile(int(self.map[i][j])), (j * 50, i * 50)) # size of single tile !

