import pygame
import Details
import TowerSlots


class GUI:
    def __init__(self):
        self.position = (900, 0)
        self.details = Details.Details((self.position[0], self.position[1] + 475))
        self.tower_slots = TowerSlots.TowerSlots((self.position[0], self.position[1] + 250))
        self.active_tower = ""

    def update(self, towers):
        all_towers = towers + self.tower_slots.get_towers()
        self.details.update(all_towers)
        self.tower_slots.update()

    def draw(self, window):
        self.details.show(window)
        self.tower_slots.show(window)
