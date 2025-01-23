import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()

    # Required print for the assignment
    #print("Starting asteroids!")
    #print(f"Screen width: {constants.SCREEN_WIDTH}")
    #print(f"Screen height: {constants.SCREEN_HEIGHT}")

    gametime = pygame.time.Clock()
    dt = 0
    #DB print(dt)

    # Setup and Init the Game Screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Adding the player and initiating groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    player1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Draw and update the player
        for object in updatable:
            object.update(dt)
        # Check for collisions
        for asteroid in asteroids:
            if(asteroid.check_collision(player1)):
                print("Game Over!")
                sys.exit()

        # Clear the screen
        screen.fill("black")

        # Add drawable objects
        for object in drawable:
            object.draw(screen)

        # Refresh the display
        pygame.display.flip()

        # Limit the FPS to 60
        dt = gametime.tick(60) / 1000
        #DB print(dt)

if __name__ == "__main__":
    main()