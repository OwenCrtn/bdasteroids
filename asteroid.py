from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS
from logger import log_event,log_state
import random



class Asteroid(CircleShape):
    def __init__(self,x:float,y:float,radius:float)->None:
        super().__init__(x,y,radius)
    
    def draw(self,screen):
        pygame.draw.circle(screen, 'white', self.position,self.radius, LINE_WIDTH)

    def update(self,dt):
        unit_vector= pygame.Vector2(0,1)
        self.position+=( self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event('asteroid_split')
        random_angle = random.uniform(20,50)
        vel_one=self.velocity.rotate(random_angle)
        vel_two=self.velocity.rotate(random.uniform(20,50))
        new_radius = self.radius -ASTEROID_MIN_RADIUS
        split_one= Asteroid(self.position.x,self.position.y,radius=new_radius)
        split_two =  Asteroid(self.position.x,self.position.y,radius=new_radius)
        
        split_one.velocity = vel_one*1.2
        split_two.velocity= vel_two*1.2





        
    