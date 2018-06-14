import pygame
import Details


class GUI:
    def __init__(self):
        self.position = (900, 0)
        self.details = Details.Details((self.position[0], self.position[1] + 475))
        self.active_tower = ""

    def update(self, towers):
        self.details.set_enabled(False)
        for tower in towers:
            tower.active = False
            if tower.get_sprite().contains(pygame.mouse.get_pos()):
                tower.active = True
                self.active_tower = tower
                self.details.set_enabled(True, self.active_tower)

    def draw(self, window):
        self.details.show(window)
