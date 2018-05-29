import Enemy, Sprite


class Enemy0(Enemy.Enemy):
    def __init__(self, start_position):
        super().__init__()
        self.health = 10
        self.speed = 10
        self.sprite = Sprite.Sprite((30, 30), start_position)
        self.next_move = self.Direction.UP
        self.previous_move = self.Direction.UP
        self.gold_dropped = 0
        self.sprite.set_fill_color((50, 50, 20))
