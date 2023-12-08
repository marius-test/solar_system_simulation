import pygame
import math
pygame.init()


WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation in Python")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SUN = (242, 131, 32)
EARTH = (66, 107, 143)
MARS = (242, 123, 95)
MERCURY = (192, 188, 189)
VENUS = (244, 219, 196)


class Planet:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 230 / AU  # 1AU = 100 pixels
    TIMESTEP = 3600 * 24  # 1 day
    
    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        
        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0
        
        self.x_velocity = 0
        self.y_velocity = 0
        
    def draw(self, win):
        x = self.x*self.SCALE + WIDTH/2
        y = self.y*self.SCALE + HEIGHT/2
        pygame.draw.circle(win, self.color, (x, y), self.radius)


def main():
    run = True
    clock = pygame.time.Clock()
    
    sun = Planet(0, 0, 30, SUN, 1.98892 * 10**30)
    sun.sun = True
    
    earth = Planet(1 * Planet.AU, 0, 16, EARTH, 5.9742 * 10*24)
    
    mars = Planet(1.524 * Planet.AU, 0, 12, MARS, 6.39 * 10**23)
    
    mercury = Planet(0.387 * Planet.AU, 0, 8, MERCURY, 0.330 * 10**24)
    
    venus = Planet(0.723 * Planet.AU, 0, 14, VENUS, 4.8685 * 10**24)

    planets = [sun, earth, mars, mercury, venus]
    
    while run:
        clock.tick(60)
        WIN.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    
        for planet in planets:
            planet.draw(WIN)
            
        pygame.display.update()
                
    pygame.quit()


main()
