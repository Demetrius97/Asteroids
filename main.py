import pygame
import sys

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


pygame.init()
gate = pygame.time.Clock()
dt = 0



def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable,)
    Player.containers = (updatable,drawable)
    Shot.containers = (shots,updatable,drawable)
    screen_color = "black"
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gamer=Player(x=SCREEN_WIDTH/2,y=SCREEN_HEIGHT/2)
    #rocks = Asteroid()
    spawn = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        screen.fill(screen_color)
        dt = gate.tick(60)/1000
        updatable.update(dt)
        for asteroid in asteroids:
             if asteroid.collides_with(gamer) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot) == True:
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()

        for obj in drawable:
            obj.draw(screen)
        # gamer.updatable(dt)
        # gamer.drawable(dt)
        pygame.display.flip()
        
        


if __name__ == "__main__":
    main()
