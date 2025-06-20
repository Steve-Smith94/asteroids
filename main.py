import sys
import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import * 


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    
    while True:
        screen.fill((0, 0, 0))
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        updateable.update(dt)
        for asteroid in asteroids:
            player.collision_check(asteroid)
            if player.collision_check(asteroid):
                print("Game over!")
                sys.exit()


print("Starting Asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

asteroids = pygame.sprite.Group()
updateable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
AsteroidField.containers = (updateable,)
asteroid_field = AsteroidField()
Asteroid.containers = (asteroids, updateable, drawable)
Player.containers = (updateable, drawable)
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)



if __name__ == "__main__":
    main()