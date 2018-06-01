import pygame

import Sprite
import Tower


class Tower0(Tower.Tower):
    def __init__(self, position):
        self.sprite = Sprite.Sprite([40, 40], position)
        self.sprite.set_fill_color((255, 0, 0))
        self.range = 100
        self.circle_range = pygame.Surface((self.range * 2, self.range * 2))
        self.circle_range.set_colorkey((0, 0, 0))
        self.circle_range.set_alpha(100)
        pygame.draw.circle(self.circle_range, (218, 161, 6), (self.range, self.range), self.range)
        self.attack_speed = 5
        self.damage = 2
