import Enemy, Sprite


class Enemy1(Enemy.Enemy):
    def __init__(self, start_position):
        super().__init__()
        self.health = 10
        self.speed = 9
        self.sprite = Sprite.Sprite((40, 40), start_position)
        self.next_move = self.Direction.UP
        self.previous_move = self.Direction.UP
        self.gold_dropped = 0
        self.sprite.set_fill_color((50, 50, 120))
