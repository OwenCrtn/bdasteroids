import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state,log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable,drawable,asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers=(drawable,updatable,shots)

    

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    field = AsteroidField()


    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000
        screen.fill("black")
        for to_draw in drawable:
            to_draw.draw(screen)
        for to_update in updatable:
            to_update.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event('player_hit')
                print('Game Over!')
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event('asteroid_shot')
                    asteroid.kill()
                    shot.kill()
            
        pygame.display.flip()


if __name__ == "__main__":
    main()
