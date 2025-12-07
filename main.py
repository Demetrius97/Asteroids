import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen_color = "black"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        screen.fill(screen_color)
        pygame.display.flip()

def fill(self,color):
    pygame.Surface.fill(color)



if __name__ == "__main__":
    main()
