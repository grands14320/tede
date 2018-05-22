import pygame


class Sprite:
    def __init__(self, size, position=(0, 0)):
        self.sprite = pygame.Surface(size)
        self.sprite.fill((255,255,255))
        self.position = position
        self.size = size
        self.rotation = 0
        self.color = (255,255,255)
        self.origin = self.sprite.get_rect()
        self.origin.center = self.position
        self.bounds = self.get_local_bounds()


    #must set size before call
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

    def set_size(self, size):
        self.size = size
        self.sprite = pygame.Surface(size)

    def get_size(self):
        return self.size

    # (position.x left up corner, position.y left up corner, size.x , size.y)
    # doesn't take sprite rotation
    def get_local_bounds(self):
        return self.origin

    def intersect(self, bounds):
        pass

    def contains(self, point):
        if self.bounds[0] < point[0] < self.bounds[0] + self.bounds[2]:
            return True
        if self.bounds[1] < point[1] < self.bounds[1] + self.bounds[3]:
            return True
        return False

    def get_surface(self):
        return self.sprite

    def draw(self, window):
        window.blit(self.sprite, self.origin)
