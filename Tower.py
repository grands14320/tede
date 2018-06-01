class Tower:
    def update(self, enemies):
        enemies_in_range = []

        for enemy in enemies:
            if(self.is_in_range(enemy)):
                enemies_in_range.append(enemy)

    def is_in_range(self, enemy):
        return False

    def draw(self, window):
        window.blit(self.circle_range, (self.sprite.get_position()[0] - self.range, self.sprite.get_position()[1] - self.range))
        self.sprite.draw(window)