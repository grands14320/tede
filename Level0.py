import Enemy0
import Level
import Sprite


class Level0(Level.Level):
    size_of_tile = (50, 50)

    def __init__(self):
        self.map = self.get_map()
        self.map_size = (15, 11)
        self.quantity_kind_of_tiles = 3
        self.tiles = [Sprite.Sprite(self.size_of_tile) for i in range(self.quantity_kind_of_tiles)]
        self.tiles[0].set_fill_color((10, 159, 85))
        self.tiles[1].set_fill_color((10, 124, 48))
        self.tiles[2].set_fill_color((103, 110, 110))

        self.enemy_start_position = (125, 625)
        self.enemy_finish_position = (175, -50)

        self.enemies = [Enemy0.Enemy0(self.enemy_start_position)]