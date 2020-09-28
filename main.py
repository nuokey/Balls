import pygame
import config as cfg
from math import sqrt
from random import randint as rnd

pygame.init()

size = (cfg.window_size_x, cfg.window_size_y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Balls | by NuoKey')

clock = pygame.time.Clock()
done = False

balls = []

class Ball():
    def __init__(self):
        self.size = rnd(15, 40)
        self.color = (rnd(1, 255), rnd(1, 255), rnd(1, 255))

        self.speed_x = rnd(1, int(self.size / size[0] * 400))
        self.speed_y = rnd(1, int(self.size / size[1] * 400))

        self.x = rnd(self.size, size[0] - self.size)
        self.y = rnd(self.size, size[1] - self.size)
    
    def draw(self):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)
    
    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def collide_update(self):
        for i in balls:
            if i != self:
                if sqrt(abs(self.x - i.x)**2 + abs(self.y - i.y)**2) <= self.size + i.size:
                    speed_x = self.speed_x
                    self.speed_x = i.speed_x
                    i.speed_x = speed_x

                    speed_y = self.speed_y
                    self.speed_y = i.speed_y
                    i.speed_y = speed_y
                
                if sqrt(abs(self.x - i.x)**2 + abs(self.y - i.y)**2) <= (self.size + i.size) / 1.3:
                    self.x += self.size
                    i.x -= i.size

    def update(self):
        if self.x + self.size >= size[0]:
            self.speed_x *= -1
            self.x -= 1
        
        if self.y + self.size >= size[1]:
            self.speed_y *= -1
            self.y -= 1

        if self.x - self.size <= 0:
            self.speed_x *= -1
            self.x += 1

        if self.y - self.size <= 0:
            self.speed_y *= -1
            self.y += 1

        self.move()
        if cfg.balls_collide:
            self.collide_update()
        
        self.draw()

for i in range(cfg.balls_number):
    balls.append(Ball())

while not done:
    clock.tick(cfg.window_fps)
    screen.fill((0, 0, 0))

    for i in balls:
        i.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pygame.display.flip()

pygame.quit()