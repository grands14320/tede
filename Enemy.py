import enum, Sprite


class Enemy:
    class Direction:
        UP = [0, -1]
        DOWN = [0, 1]
        LEFT = [-1, 0]
        RIGHT = [1, 0]

    def __init__(self):
        self.health = 10
        self.speed = 10
        self.sprite = Sprite.Sprite((50, 50), (100, 500))
        self.next_move = Enemy.Direction.UP
        self.previous_move = Enemy.Direction.UP
        self.gold_dropped = 0
        self.sprite.set_fill_color((50, 50, 20))

    def move(self, map):
        if self.set_direction(map):
            moveOffset = (self.next_move[0] * self.speed, self.next_move[1] * self.speed)
            self.sprite.move(moveOffset)

    def set_direction(self, map):

        print(self.sprite.get_position())
        print(self.sprite.get_position()[1] - 20)
        x = round(self.sprite.position[0] / 50)
        y = round(self.sprite.position[1] / 50)

        print('x', x)
        print('y', y)
        print('y',y*50)
        if self.sprite.get_position()[0] % 50 != 0 and self.sprite.get_position()[1] + 20 % 50 != 0:
            print("wykonalem sie")
            # return True

            if map[y + 1][x] == '3' and self.previous_move != Enemy.Direction.UP:  # dol
                print("wykonal sie dol")
                self.next_move = Enemy.Direction.DOWN
                self.previous_move = Enemy.Direction.DOWN
                return True

            elif map[y - 1][x] == '3' and self.previous_move != Enemy.Direction.DOWN:  # gora
                print("wykonal sie gora")
                self.next_move = Enemy.Direction.UP
                self.previous_move = Enemy.Direction.UP
                return True

            elif map[y][x + 1] == '3' and self.previous_move != Enemy.Direction.LEFT:  # prawo
                print("wykonal sie prawo")
                self.next_move = Enemy.Direction.RIGHT
                self.previous_move = Enemy.Direction.RIGHT
                return True

            elif map[y][x - 1] == '3' and self.previous_move != Enemy.Direction.RIGHT:  # lewo
                print("wykonal sie lewo")
                self.next_move = Enemy.Direction.LEFT
                self.previous_move = Enemy.Direction.LEFT
                return True

            else:
                return False

    def enemy_death(self):
        if self.health < 0:
            del self
        if self.sprite.origin == (100, 0): #dopoprawy
            del self

    def draw(self, window):
        self.sprite.draw(window)