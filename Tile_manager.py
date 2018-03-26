import Sprite


class TileManager:
    def __init__(self):
        self.sprite = Sprite.Sprite((60, 60))
        self.tiles = [self.sprite.sprite,
                      self.sprite.sprite,
                      self.sprite.sprite]

    def get_tile(self, point):
        return self.tiles[int(point) - 1]
