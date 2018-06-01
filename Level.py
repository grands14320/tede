import time

import pygame

import Enemy1

class Level:
    size_of_tile = (0, 0)

    def get_tile(self, point):
        return self.tiles[point-1].get_surface()

    def get_map(self,current_level):
        map_list = []
        level = "Levels/" + "Level_" + str(current_level) + "/map"
        with open(level, 'r') as file:
            for line in file.readlines():
                line = line.strip('\n')
                map_list.append(line.split("  "))
        return map_list

    def update(self, window):
        i = 0
        while i < len(self.enemies):
            if self.enemies[i].arrived_to_finish(self.enemy_finish_position):
                self.enemies.pop(i)
                continue
            self.enemies[i].move(self.map, self.map_size)
            i += 1

        if time.clock() > 2 > len(self.enemies):
            self.enemies.append(Enemy1.Enemy1(self.enemy_start_position))

        self.draw_map(window)

        for enemy in self.enemies:
            enemy.draw(window)

        for tower in self.towers:
            tower.update(self.enemies)
            tower.draw(window)

    def draw_map(self, window):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                window.blit(self.get_tile(int(self.map[i][j])), (j * self.size_of_tile[0], i * self.size_of_tile[1]))
