# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        player.update(dt) # placed by boot.dev

        pygame.Surface.fill(screen, (0,0,0)) # written by me
        # pygame.Surface.fill(screen, color = "black") # written by me
        # screen.fill("black") # from boot.dev solution
        player.draw(screen)
        # player.update(dt) # placed by me
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = fps.tick(60) / 1000

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()