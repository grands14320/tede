import pygame

class Sprite:
    def __init__(self, size, position=(0, 0)):
        self.sprite = pygame.Surface(size)
        self.sprite.fill((255,255,255))
        self.position = position
        self.size = size
        self.rotation = 0
        self.color = (255,255,255)
        self.origin = (0, 0)

    def set_texture(self, path):
        self.sprite = pygame.image.load(path)

    def set_position(self, new_position):
        self.position = new_position

    def move(self, offset=(0, 0)):
        self.position = tuple(map(lambda x, y: x + y, self.position, offset))

    def set_rotation(self, new_rotation):
        self.rotation = new_rotation % 360
        self.sprite = pygame.Surface(self.size)
        self.sprite.fill(self.color)
        self.sprite.set_colorkey((0, 0, 0))
        self.sprite = pygame.transform.rotate(self.sprite, self.rotation)
        self.origin = self.sprite.get_rect()
        self.origin.center = self.position

    def rotate(self, angle=0):
        self.rotation += angle
        self.rotation %= 360
        self.set_rotation(self.rotation)

    def set_fill_color(self, color):
        self.color = color
        self.sprite.fill(self.color)

    def draw(self, window):
        window.blit(self.sprite, self.origin)
s