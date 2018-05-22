import Sprite, Level


class Level0(Level.Level):
    def __init__(self):
        Level.Level.__init__(self)
        self.tiles = [Sprite.Sprite((50, 50)),
                      Sprite.Sprite((50, 50)),
                      Sprite.Sprite((50, 50))]  # fill() ?
        self.tiles[0].set_fill_color((10, 159, 85))
        self.tiles[1].set_fill_color((10, 124, 48))
        self.tiles[2].set_fill_color((103, 110, 110))
        self.enemy_quantity = 1
