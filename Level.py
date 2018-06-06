import time
from Utility import Tools
import Enemy1, Enemy0


class Level:

    def __init__(self):
        self.money = 0
        self.hp = 100
        self.waves = Tools.get_single_wave()
        self.wave = self.get_wave()
        self.time_start_lvl = 0
        self.enemies_type = [Enemy0.Enemy0((125, 625)), Enemy1.Enemy1((125, 625))]

    def get_tile(self, point):
        return self.tiles[point - 1].get_surface()

    def get_map(self, current_level):
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
            if self.enemies[i].get_health() <= 0:
                self.money += self.enemies[i].get_gold_dropped()
                self.enemies.pop(i)
            if self.enemies[i].arrived_to_finish(self.enemy_finish_position):
                self.hp -= 10
                self.enemies.pop(i)
                continue
            self.enemies[i].move(self.map, self.map_size)
            i += 1

        self.update_wave()

        if len(self.enemies) == 0:  # narazie jesli brak enemy,pozniej jezeli user wcisnie guzik czy cos
            self.wave = self.get_wave()
            self.time_start_lvl = time.clock()

        self.draw_map(window)

        for enemy in self.enemies:
            enemy.draw(window)

        for tower in self.towers:
            tower.update(self.enemies)
            tower.draw(window)

        if self.hp <= 0:
            self.game_over()

    def game_over(self):
        pass

    def draw_map(self, window):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                window.blit(self.get_tile(int(self.map[i][j])), (j * self.size_of_tile[0], i * self.size_of_tile[1]))

    def get_wave(self):
        for _, dictionary in self.waves:
            return dictionary

    def update_wave(self):
        i = 0
        print(self.enemies)
        while i < len(self.wave.items()):
            spawn_time = list(self.wave.items())[i][0]
            enemy_type = list(self.wave.items())[i][1]
            print(round(time.clock(), 5), round(self.time_start_lvl, 5), spawn_time)

            if (round(time.clock(), 5) - round(self.time_start_lvl, 5)) > float(spawn_time):
                print("wykonalem sie")
                break

            self.enemies.append(self.enemies_type[int(enemy_type)].clone())
            del self.wave[spawn_time]
