from circleshape import *


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, dt):
        #print(f"Shot at position: {self.position}")
        self.position = self.velocity * dt + self.position

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)