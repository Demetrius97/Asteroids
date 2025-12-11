# Asteroid Class
from logger import log_event
from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self, dt):
        self.position = self.position + self.velocity*dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20,50)
        A1_velocity = self.velocity.rotate(angle)
        A2_velocity = self.velocity.rotate(-1 * angle)
        radius = self.radius - ASTEROID_MIN_RADIUS
        A1_velocity *= 1.2
        A2_velocity *= 1.2
        A1 = Asteroid(self.position.x,self.position.y,radius)
        A2 = Asteroid(self.position.x,self.position.y,radius)
        A1.velocity = A1_velocity
        A2.velocity = A2_velocity
            


    
