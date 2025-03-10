# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    rocks = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (rocks, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt) # placed by boot.dev
        for rock in rocks:
            if rock.collision(player):
                print("Game over!")
                sys.exit()

        pygame.Surface.fill(screen, (0,0,0)) # written by me
        # screen.fill("black") # from boot.dev solution
        
        for obj in drawable:
            obj.draw(screen)
        # player.update(dt) # placed by me
        
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = fps.tick(60) / 1000

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()