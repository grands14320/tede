import Sprite


class Level:
    def __init__(self):
        self.tiles = []

    def get_tile(self, point):
        return self.tiles[point-1].get_surface()
