import pygame, point

class GameObject(pygame.sprite.Sprite):

    def __init__(self, location, radius):

        self.loc = location
        self.radius = radius
        self.size = radius * 2 + 1

        self.rect = pygame.Rect(self.loc.x - self.radius, self.loc.y + self.radius, self.size, self.size)
        
