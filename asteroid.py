import pygame
import random
from circleshape import CircleShape
from constants import *
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:

        super().__init__(x, y, radius)

    def draw(self, screen):

        pygame.draw.circle(screen, "white", self.position, self.radius, width = LINE_WIDTH)

    def update(self, dt):

        self.position += (self.velocity * dt)

    def split(self):

        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:

            return

        else:
            log_event("asteroid_split")

            temp_angle = random.uniform(20, 50)

            temp_rad = self.radius - ASTEROID_MIN_RADIUS

            asteroid = Asteroid(self.position.x, self.position.y, temp_rad)
            asteroid.velocity = self.velocity.rotate(temp_angle * 1.2)
            asteroid = Asteroid(self.position.x, self.position.y, temp_rad)
            asteroid.velocity = self.velocity.rotate(temp_angle * -1.2)
