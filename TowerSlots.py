import pygame

import Sprite
import Tower0
import Tower1
import Tower2
import TowerSlot


class TowerSlots:

    def __init__(self, position):
        self.position = position
        self.size = (200, 200)
        self.background = Sprite.Sprite(self.size, self.position)
        self.background.set_fill_color((123, 170, 123))

        self.towers = [Tower0.Tower0([0, 0]),
                       Tower1.Tower1([0, 0]),
                       Tower2.Tower2([0, 0])]

        self.slot_size = (50, 50)
        self.slots = []
        self.active_slot = ""
        self.mouse_clicked = False
        self.create_slots()


    def create_slots(self):
        slots_in_row = 3
        margin = int(((self.size[0]) - 10) - self.slot_size[0] * slots_in_row) / slots_in_row
        bounds = self.background.get_global_bounds()
        x = bounds[0] + margin
        y = bounds[1] + 10

        for i in range(0, len(self.towers)):
            self.slots.append(TowerSlot.TowerSlot(self.towers[i], (x + self.slot_size[0] / 2, y + self.slot_size[1] / 2), self.slot_size))
            x += self.slot_size[0] + margin
            if (i + 1) % slots_in_row == 0:
                x = bounds[0] + margin
                y += self.slot_size[1] + 10

        self.slots[2].locked = True

    def get_towers(self):
        enabled_towers = []
        for slot in self.slots:
            if not slot.locked:
                enabled_towers.append(slot.get_tower())
        return enabled_towers

    def update(self):
        for slot in self.slots:
            if self.mouse_clicked == False and slot.clicked():
                if self.active_slot != "":
                    self.active_slot.set_unactive()
                    self.mouse_clicked = True
                if self.active_slot == slot:
                    self.active_slot = ""
                else:
                    self.active_slot = slot

        if not pygame.mouse.get_pressed()[0]:
            self.mouse_clicked = False


    def show(self, window):
        self.background.draw(window)

        active_slot = ""
        for slot in self.slots:
            if not slot.get_tower().is_active():
                slot.draw(window)
            else:
                active_slot = slot
        if active_slot != "":
            active_slot.draw(window)
