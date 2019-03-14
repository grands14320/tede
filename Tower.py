import math
import time

from Bullet import Bullet
from Sprite import Sprite
from Utility import Tools


class Tower:
    def __init__(self):
        self.finded = False
        self.time_last_shoot = 0
        self.kills = 0
        self.bullets = []
        self.active = False
        self.rotated = False

    def get_damage(self):
        return self.damage

    def get_cooldown(self):
        return self.cooldown

    def get_range(self):
        return self.range

    def get_kills(self):
        return self.kills

    def get_sprite(self):
        return self.sprite

    def update(self, enemies):

        self.finded = False
        target = ""
        distance = 0

        for enemy in enemies:
            if self.is_in_range(enemy) and enemy.get_distance_travelled() > distance:
                target = enemy
                distance = enemy.get_distance_travelled()
                self.finded = True

        if self.finded and self.rotatable:
            self.rotate_to_target(target.get_sprite().get_position())

        if self.can_shoot():
            self.time_last_shoot = time.clock()
            self.shoot_to_target(target)

        i = 0
        while i < len(self.bullets):
            bullet_position = self.bullets[i].get_sprite().get_position()
            if self.hitted_enemy(self.bullets[i], enemies):
                self.bullets.pop(i)
                continue
            if Tools.get_length_point_to_point(bullet_position, self.sprite.get_position()) > self.range:
                self.bullets.pop(i)
                continue
            self.bullets[i].update()
            i += 1

    def is_in_range(self, enemy):

        bounds = enemy.get_sprite().get_global_bounds()

        # left up corner
        if Tools.get_length_point_to_point((bounds[0], bounds[1]), self.position) <= self.range:
            return True
        # right up
        if Tools.get_length_point_to_point((bounds[0] + bounds[2], bounds[1]), self.position) <= self.range:
            return True
        # right down
        if Tools.get_length_point_to_point((bounds[0] + bounds[2], bounds[1] + bounds[3]), self.position) <= self.range:
            return True
        # left down
        if Tools.get_length_point_to_point((bounds[0], bounds[1] + bounds[3]), self.position) <= self.range:
            return True
        return False

    def can_shoot(self):
        if self.finded == False:
            return False

        if self.rotated == False and self.rotatable:
            return False

        if time.clock() - self.time_last_shoot <= self.cooldown:
            return False

        return True

    def rotate_to_target(self, target):
        rotation = math.fmod(self.sprite.get_rotation_to_point(target), 360)
        object_rotation = self.sprite.get_rotation()
        dif = rotation - object_rotation
        self.rotated = False
        if dif < -181:
            dif = 360 - self.sprite.get_rotation() + rotation
        elif dif > 181:
            dif = -(360 - rotation + self.sprite.get_rotation())

        if dif > 2:
            self.sprite.rotate(self.rotation_speed)
        elif dif < -2:
            self.sprite.rotate(-self.rotation_speed)
        else:
            self.rotated = True

    def shoot_to_target(self, target):
        tower_position = self.sprite.get_position()
        enemy_position = target.get_sprite().get_position()
        vector = (enemy_position[0] - tower_position[0], enemy_position[1] - tower_position[1])
        vector_length = Tools.get_length_point_to_point(tower_position, enemy_position)
        vector = (vector[0] / vector_length, vector[1] / vector_length)
        self.bullets.append(Bullet(Sprite((10, 10), self.sprite.get_position()), vector, self.bullet_speed))

    def hitted_enemy(self, bullet, enemies):
        i = 0
        while i < len(enemies):
            if enemies[i].get_sprite().intersect(bullet.get_sprite().get_global_bounds()):
                enemies[i].health -= self.damage
                if enemies[i].health <= 0:
                    self.kills += 1
                print("Trafiony")
                return True
            i += 1
        return False

    def draw(self, window):
        if self.active:
            window.blit(self.circle_range,
                        (self.sprite.get_position()[0] - self.range, self.sprite.get_position()[1] - self.range))
        self.sprite.draw(window)

        for bullet in self.bullets:
            bullet.draw(window)
