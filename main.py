import pygame
from pygame.locals import *
import constants
from constants import *
import player
from player import *

def main():
    pygame.init()

    #Required print for the assignment
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    gametime = pygame.time.Clock()
    dt = 0
    dt = gametime.tick(60)/1000

    #Setup and Init the Game Screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #adding the player
    player1 = player.Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        
        player1.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()