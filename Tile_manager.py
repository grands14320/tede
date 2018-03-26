import Sprite


class TileManager:
    def __init__(self):
        self.sprite = Sprite.Sprite((60, 60))
        self.tiles = [self.sprite.set_fill_color((10, 159, 85)),  # light green
                      self.sprite.set_fill_color((10, 124, 48)),  # dark green
                      self.sprite.set_fill_color((103, 110, 110))  # path
                      ]

    def get_tile(self, point):
        print(self.tiles[0])
        return self.tiles[int(point)]
