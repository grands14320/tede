import Sprite, Level, Enemy, Game

class Level0(Level.Level):

    def __init__(self):
        Level.Level.__init__(self)
        self.map = self.get_map()
        self.tiles = [Sprite.Sprite((50, 50)),
                      Sprite.Sprite((50, 50)),
                      Sprite.Sprite((50, 50))]

        self.tiles[0].set_fill_color((10, 159, 85))
        self.tiles[1].set_fill_color((10, 124, 48))
        self.tiles[2].set_fill_color((103, 110, 110))

        self.size_of_single_tile = (50, 50)

        self.enemy = Enemy.Enemy();

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
                window.blit(self.get_tile(int(self.map[i][j])), (j * self.size_of_single_tile[0], i * self.size_of_single_tile[1]))

    def update(self, window):
        self.enemy.move(self.map)

        self.draw_map(window)
        self.enemy.draw(window)