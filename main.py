import pygame
import constants
from constants import *
import player
from player import *

def main():
    pygame.init()

    #Required print for the assignment
    #print("Starting asteroids!")
    #print(f"Screen width: {constants.SCREEN_WIDTH}")
    #print(f"Screen height: {constants.SCREEN_HEIGHT}")

    gametime = pygame.time.Clock()
    dt = 0
    #DB print(dt)

    #Setup and Init the Game Screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #adding the player and initiating groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    player1 = player.Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Clear the screen
        screen.fill("black")
        
        # Update and draw the player
        for object in updatable:
            object.update(dt)
        for object in drawable:
            object.draw(screen)

        # Refresh the display
        pygame.display.flip()

        # Limit the FPS to 60
        dt = gametime.tick(60) / 1000
        #DB print(dt)

if __name__ == "__main__":
    main()