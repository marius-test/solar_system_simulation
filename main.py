import pygame
import math
pygame.init()


WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation in Python")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SUN = (242, 131, 32)
MERCURY = (192, 188, 189)
VENUS = (244, 219, 196)
EARTH = (66, 107, 143)
MARS = (242, 123, 95)
JUPITER = (191, 175, 155)
SATURN = (218, 183, 120)
URANUS = (149, 187, 190)
NEPTUNE = (101, 123, 165)
PLUTO =  (244, 235, 220)


FONT = pygame.font.SysFont("courier new", 16)


class Planet:
    AU = 149.6e6 * 1000  # meters
    G = 6.67428e-11  # newtons
    SCALE = 250 / AU  # 1AU = 100 pixels
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
        
        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x*self.SCALE + WIDTH/2
                y = y*self.SCALE + HEIGHT/2
                updated_points.append((x, y))
        
            pygame.draw.lines(win, self.color, False, updated_points, 2)
        
        pygame.draw.circle(win, self.color, (x, y), self.radius)
        
        if not self.sun:
            distance_text = FONT.render(f"{round(self.distance_to_sun/1000, 1)}km", 1, WHITE)
            win.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_width()/2))
        
    def attraction (self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x**2 + distance_y**2)
        
        if other.sun:
            self.distance_to_sun = distance
            
        force = self.G * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y
    
    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue
            
            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy
            
        self.x_velocity += total_fx / self.mass * self.TIMESTEP
        self.y_velocity += total_fy / self.mass * self.TIMESTEP
        
        self.x += self.x_velocity * self.TIMESTEP
        self.y += self.y_velocity * self.TIMESTEP
        self.orbit.append((self.x, self.y))


def main():
    run = True
    clock = pygame.time.Clock()
    
    sun = Planet(0, 0, 30, SUN, 1.989 * 10**30)
    sun.sun = True
    
    mercury = Planet(0.387 * Planet.AU, 0, 2.43, MERCURY, 0.330 * 10**24)
    mercury.y_velocity = 47.4 * 1000  # meters/second
    
    venus = Planet(0.723 * Planet.AU, 0, 6.05, VENUS, 4.87 * 10**24)
    venus.y_velocity = 35.02 * 1000  # meters/second
    
    earth = Planet(1 * Planet.AU, 0, 6.37, EARTH, 5.97 * 10*24)
    earth.y_velocity = 29.783 * 1000  # meters/second
    
    mars = Planet(1.524 * Planet.AU, 0, 3.39, MARS, 0.642 * 10**24)
    mars.y_velocity = 24.077 * 1000  # meters/second
    
    jupiter = Planet(5.20 * Planet.AU, 0, 71.4, JUPITER, 1898 * 10**24)
    jupiter.y_velocity = 13.1 * 1000  # meters/second
    
    saturn = Planet(9.54 * Planet.AU, 0, 60.2, SATURN, 568 * 10**24)
    saturn.y_velocity = 9.7 * 1000  # meters/second
    
    uranus = Planet(19.20 * Planet.AU, 0, 25.5, URANUS, 86.8 * 10**24)
    uranus.y_velocity = 6.8 * 1000  # meters/second
    
    neptune = Planet(30.06 * Planet.AU, 0, 24.7, NEPTUNE, 102 * 10**24)
    neptune.y_velocity = 5.4 * 1000  # meters/second
    
    pluto = Planet(39.5 * Planet.AU, 0, 1.18, PLUTO, 0.0130 * 10**24)
    pluto.y_velocity = 4.7 * 1000  # meters/second
    
    planets = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto]
    
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
            planet.update_position(planets)
            planet.draw(WIN)
            
        pygame.display.update()
                
    pygame.quit()


main()
