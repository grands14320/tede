import Sprite


class TileManager:
    def __init__(self):

        # size of single tile !

        self.tiles = [Sprite.Sprite((60, 60)),
                      Sprite.Sprite((60, 60)),
                      Sprite.Sprite((60, 60))] # fill() ?

        self.tiles[0].set_fill_color((10,159,85))
        self.tiles[1].set_fill_color((10,124,48))
        self.tiles[2].set_fill_color((103,110,110))

    def get_tile(self, point):
        return self.tiles[point-1].get_surface()
