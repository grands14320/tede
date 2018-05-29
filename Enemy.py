import Sprite
import Game


class Enemy:
    class Direction:
        UP = [0, -1]
        DOWN = [0, 1]
        LEFT = [-1, 0]
        RIGHT = [1, 0]

    def __init__(self):
        self.health = 10
        self.speed = 25
        self.sprite = Sprite.Sprite((40, 40))
        self.next_move = Enemy.Direction.UP
        self.previous_move = Enemy.Direction.UP
        self.gold_dropped = 0
        self.sprite.set_fill_color((50, 50, 20))

    def __del__(self):
        print("dyntka")

    def move(self, map, map_size):

        size_of_tile = Game.Game.levels[Game.Game.current_level].size_of_tile

        x = int(self.sprite.get_position()[0] / size_of_tile[0])
        y = int(self.sprite.get_position()[1] / size_of_tile[1])

        moveOffset = [self.next_move[0] * self.speed, self.next_move[1] * self.speed]

        if not self.is_on_center_tile(x, y, map_size):

            position_of_tile = (x * size_of_tile[0] + size_of_tile[0] / 2,
                                y * size_of_tile[1] + size_of_tile[1] / 2)

            length_from_tile = [(position_of_tile[0] - self.sprite.get_position()[0]),
                                (position_of_tile[1] - self.sprite.get_position()[1])]

            if abs(moveOffset[0]) > abs(length_from_tile[0]) or abs(moveOffset[1]) > abs(length_from_tile[1]):
                self.sprite.move(length_from_tile)
                self.set_direction(map, map_size)
                moveOffset = [self.next_move[0] * self.speed, self.next_move[1] * self.speed]

        else:
            self.set_direction(map, map_size)
            moveOffset = [self.next_move[0] * self.speed, self.next_move[1] * self.speed]

        self.sprite.move(moveOffset)
        self.sprite.rotate(20)

    def set_direction(self, map, map_size):
        size_of_tile = Game.Game.levels[Game.Game.current_level].size_of_tile

        x = int(self.sprite.get_position()[0] / size_of_tile[0])
        y = int(self.sprite.get_position()[1] / size_of_tile[1])

        if x - 1 < 0 or x + 1 > map_size[0] or y - 1 < 0 or y + 1 > map_size[1]:
            return True

        if map[y + 1][x] == '3' and self.previous_move != Enemy.Direction.UP:  # down
            self.next_move = Enemy.Direction.DOWN
            self.previous_move = Enemy.Direction.DOWN
            return True

        if map[y - 1][x] == '3' and self.previous_move != Enemy.Direction.DOWN:  # up
            self.next_move = Enemy.Direction.UP
            self.previous_move = Enemy.Direction.UP
            return True

        if map[y][x + 1] == '3' and self.previous_move != Enemy.Direction.LEFT:  # right
            self.next_move = Enemy.Direction.RIGHT
            self.previous_move = Enemy.Direction.RIGHT
            return True

        if map[y][x - 1] == '3' and self.previous_move != Enemy.Direction.RIGHT:  # left
            self.next_move = Enemy.Direction.LEFT
            self.previous_move = Enemy.Direction.LEFT
            return True

    def is_on_center_tile(self, x, y, map_size):
        size_of_tile = Game.Game.levels[Game.Game.current_level].size_of_tile

        if x - 1 < 0 or x + 1 > map_size[0] or y - 1 < 0 or y + 1 > map_size[1]:
            return True

        return not (x * size_of_tile[0] + size_of_tile[0] / 2 != self.sprite.get_position()[0] or y * size_of_tile[1] + size_of_tile[1] / 2 != self.sprite.get_position()[1])

    def arrived_to_finish(self, finish):
        size_of_tile = Game.Game.levels[Game.Game.current_level].size_of_tile

        sprite_index_x = int(self.sprite.get_position()[0] / size_of_tile[0])
        sprite_index_y = int(self.sprite.get_position()[1] / size_of_tile[1])

        finish_index_x = int(finish[0] / size_of_tile[0])
        finish_index_y = int(finish[1] / size_of_tile[1])

        return sprite_index_x == finish_index_x and sprite_index_y == finish_index_y

    def draw(self, window):
        self.sprite.draw(window)
