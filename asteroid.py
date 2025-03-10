import pygame
import random
from constants import *
from circleshape import CircleShape



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self,):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        rand_num = random.uniform(20, 50)
        a = self.velocity.rotate(rand_num)
        b = self.velocity.rotate(-rand_num)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        rock1 = Asteroid(self.position.x, self.position.y, new_radius)
        rock1.velocity = a * 1.2
        rock2 = Asteroid(self.position.x, self.position.y, new_radius)
        rock2.velocity = b * 1.2