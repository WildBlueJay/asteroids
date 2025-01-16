import pygame
from pygame.locals import *
import constants
from constants import *

def main():
    pygame.init()

    #Required print for the assignment
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    #Setting Up and Init the Game Screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0), rect=None, special_flags=0)
        pygame.display.flip()

if __name__ == "__main__":
    main()