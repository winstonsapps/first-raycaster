import math
import pygame
class Player:
    def __init__(self, x, y, size, map):
        print(map)
        self.rect = pygame.Rect(x,y,size,size)
        self.map = map
        self.direction = 0



    def try_move(self, dx,dy): 
        """ moves with collision """
        self.rect.move(dx, dy)
        if not self.rect.collidelist(self.map) == -1:
            self.rect.move(-dx, -dy)

    def move(self, distance): # math for movement
        self.try_move(distance*math.sin(math.radians(self.direction)), 0)
        self.try_move(0, distance*math.cos(math.radians(self.direction)))

class Raycaster:
    def __init__(self, map):
        self.rect = pygame.Rect(0,0,0,0)
        self.map = map  # map
    def goto(self, x, y): # goes to coordinate
        self.rect.x = x
        self.rect.y = y
    def move(self, steps, direction):
        self.rect.move(math.floor(steps*math.sin(math.radians(direction))), math.floor(steps*math.cos(math.radians(direction))))
    def single_ray(self, playerx, playery, direction): # casts ray and returns distance
        self.goto(playerx, playery)
        while not  self.rect.collidelist(self.map) == -1:
            self.move(2, direction)
        while self.rect.collidelist(self.map) == -1:
            self.move(-1, direction)
        return math.dist((playerx, playery), (self.rect.x, self.rect.y))

    

    