from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH) 

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(angle)
        v2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_ast = Asteroid(self.position.x, self.position.y, new_radius)
        new_ast2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_ast.velocity = v1 * 1.2
        new_ast2.velocity = v2 * 1.2
