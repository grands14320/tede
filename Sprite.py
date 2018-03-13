import pygame

class Sprite:
    def __init__(self, size=(0, 0), position=(0, 0), color=(0, 0, 0)):
        self.sprite = pygame.Surface(size)
        self.sprite.fill(color)
        self.position = position
        self.size = size
        self.rotation = 0
        self.color = color
        self.origin = (0, 0)

    def setPosition(self, newPosition=(0, 0)):
        self.position = newPosition

    def move(self, offset=(0, 0)):
        self.position = tuple(map(lambda x, y: x + y, self.position, offset))

    def setRotation(self, newRotation=0):
        self.rotation = newRotation
        self.sprite = pygame.Surface(self.size)
        self.sprite.fill(self.color)
        self.sprite.set_colorkey((0, 0, 0))
        self.sprite = pygame.transform.rotate(self.sprite, self.rotation)
        self.origin = self.sprite.get_rect()
        self.origin.center = self.position

    def rotate(self, angle=0):
        self.rotation += angle
        self.rotation %= 360
        self.setRotation(self.rotation)

    def draw(self, window):
        window.blit(self.sprite, self.origin)
