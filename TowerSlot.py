import pygame

import Sprite


class TowerSlot:
    def __init__(self, tower, position, size):
        self.tower = tower
        self.tower.enabled = False
        self.position = position
        self.tower.get_sprite().set_position(self.position)
        self.size = size
        self.background = Sprite.Sprite(self.size, self.position)
        self.background.set_fill_color((123, 0, 0))
        self.inactive = Sprite.Sprite(self.size, self.position)
        self.inactive.set_fill_color((123, 123, 123, 200))
        self.locked = False
        self.active = False

    def get_tower(self):
        return self.tower

    def set_active(self):
        self.background.set_fill_color((0, 160, 0))

    def set_unactive(self):
        self.background.set_fill_color((123, 0, 0))

    def clicked(self):
        if self.tower.get_sprite().contains(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[
            0] and self.locked == False:
            self.set_active()
            return True
        return False

    def draw(self, window):
        self.background.draw(window)
        self.tower.draw(window)

        if self.locked:
            self.inactive.draw(window)
