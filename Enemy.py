import enum, Sprite, Map


class Enemy:
    class Direction(enum.Enum):
        UP = (-1, 0)
        DOWN = (1, 0)
        LEFT = (0, -1)
        RIGHT = (0, 1)

    def __init__(self):
        self.health = 0
        self.speed = 0
        self.sprite = Sprite.Sprite
        self.next_move = Enemy.Direction.UP
        self.previous_move = Enemy.Direction.DOWN

        self.gold_dropped = 0
        # self.map = Map.Map

    def make_move(self):        #do poprawy
        new_position_x = self.next_move[0] * self.speed
        new_position_y = self.next_move[1] * self.speed
        self.sprite.set_position((new_position_x, new_position_y))

    def set_direction(self, mapa):
        x = int(self.sprite.position[0] / 50)
        y = int(self.sprite.position[1] / 50)

        if mapa[x + 1][y] == 3:    # dol
            if self.previous_move != Enemy.Direction.UP:
                self.next_move = Enemy.Direction.DOWN

        elif mapa[x - 1][y] == 3:  # gora
            if self.previous_move != Enemy.Direction.DOWN:
                self.next_move = Enemy.Direction.UP

        elif mapa[x][y + 1] == 3:  # prawo
            if self.previous_move != Enemy.Direction.LEFT:
                self.next_move = Enemy.Direction.RIGHT

        elif mapa[x][y - 1] == 3:  # lewo
            if self.previous_move != Enemy.Direction.RIGHT:
                self.next_move = Enemy.Direction.LEFT

        else:
            print("nie znaleziono mozliwej drogi")

    def enemy_death(self):
        if self.health < 0:
            del self  # tu powinna byc chyba deinicjalizacja tego przeciwnika (nie wiem czy to dobrze jest)
