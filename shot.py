import pygame

from constants import SHOT_RADIUS,LINE_WIDTH
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self,x,y):
        super().__init__(x, y, SHOT_RADIUS)
        self.x = x
        self.y =y
        self.SHOT_RADIUS = SHOT_RADIUS

    def draw(self,screen):
        pygame.draw.circle(screen, 'white', self.position,self.radius, LINE_WIDTH)
    
    def update(self,dt):
        unit_vector= pygame.Vector2(0,1)
        self.position+=( self.velocity * dt)
