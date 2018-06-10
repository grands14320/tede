import Details


class GUI:
    def __init__(self):
        self.position = (900, 0)
        self.details = Details.Details((self.position[0], self.position[1] + 475))
        self.active_tower = ""

    def update(self, towers):
        # if clicked
        self.active_tower = towers[0]
        self.details.set_enabled(True, self.active_tower)

    def draw(self, window):
        self.details.show(window)