import enum, Sprite, Map


class Enemy:
    class Direction:
        UP = [0, -1]
        DOWN = [1, 0]
        LEFT = [0, 1]
        RIGHT = [0, -1]

    def __init__(self):
        self.health = 10
        self.speed = 10
        self.sprite = Sprite.Sprite((50, 50), (125, 525))
        self.next_move = Enemy.Direction.UP
        self.previous_move = Enemy.Direction.DOWN
        self.gold_dropped = 0
        self.sprite.set_fill_color((50, 50, 20))

    def make_move(self, current_x, current_y):
        new_position_x = self.next_move[0] * self.speed
        new_position_y = self.next_move[1] * self.speed
        self.sprite.origin[0] = new_position_x + current_x
        self.sprite.origin[1] = new_position_y + current_y

    def set_direction(self, mapa): #to nie dziala
        print('x', self.sprite.origin[0])
        print('y ', self.sprite.origin[1])

        x = int(self.sprite.origin[0] / 50)
        y = int(self.sprite.origin[1] / 50) + 1
        print('x', x)
        print('y', y)
        print(mapa[x + 1][y])
        if mapa[x + 1][y] == '3':  # dol
            print("wykonal sie dol")
            if self.previous_move != Enemy.Direction.UP:
                self.next_move = Enemy.Direction.DOWN

        elif mapa[x - 1][y] == '3':  # gora
            print("wykonal sie gora")
            if self.previous_move != Enemy.Direction.DOWN:
                self.next_move = Enemy.Direction.UP

        elif mapa[x][y + 1] == '3':  # prawo
            print("wykonal sie prawo")
            if self.previous_move != Enemy.Direction.LEFT:
                self.next_move = Enemy.Direction.RIGHT

        elif mapa[x][y - 1] == '3':  # lewo
            print("wykonal sie lewo")
            if self.previous_move != Enemy.Direction.RIGHT:
                self.next_move = Enemy.Direction.LEFT
        else:
            print("nie znaleziono mozliwej drogi")

    def enemy_death(self):
        if self.health < 0:
            del self
        if self.sprite.origin == (100, 0): #dopoprawy
            del self

    # def rys(self):
