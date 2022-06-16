import pygame
import math
import player as player1
import random

def distance(rect1, rect2):
    point1 = (rect1.x, rect1.y)
    point2 = (rect2.x, rect2.y)
    return math.dist(point1, point2)

""" pygame setup: """
pygame.init()
size = 1000 # modify
screen = pygame.display.set_mode((size, size)) # creates window
clock = pygame.time.Clock()
pygame.key.set_repeat(5)
""" end pygame setup """

""" colors """
white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)


""" end colors """
""" keybind setup (movement, rotation, rotation offset) """

speed = 1 # speed in pixels 
rotation_speed = 1 # rotation speed in degrees

MOVEMENT_KEYBINDS = { # nice keybinds that are easy to modify 
    pygame.K_UP :    (speed, 0, 0), # move forwards
    pygame.K_DOWN :  (-speed, 0, 0), # move backwards
    pygame.K_LEFT :  (0, rotation_speed, 0), # turn left
    pygame.K_RIGHT :  (0, -rotation_speed, 0), # turn right
    pygame.K_w :    (speed, 0, 0), # move forwards
    pygame.K_s :  (-speed, 0, 0), # move backwards
    pygame.K_a :  (0, speed, 90), # strafe left
    pygame.K_d :  (0, speed, -90),# strafe right
}

""" end keybind setup """

""" map setup """

maptext = [] # creates maptext list for parsing
map = [] # will be filled with rects
mapsize = 20 # size should be divisible by it
map_part_size = int(size/mapsize) # size of each rect in the map
load = input("load file (Y/N): ") # asks user if they want to load a file
if load != "Y":
    for i in range(mapsize):
        maptext.append([]) # adds new row
        for j in range(mapsize):
            random_number = random.randint(0,2)
            if random_number == 0 or i == 0 or i == mapsize-1 or j == 0 or j == mapsize-1:
                maptext[i].append("#") #add wall
            else:
                maptext[i].append("*")  #add space
if load == "Y":
    file_name = input("enter file name: ") # asks user to enter the file name
    file_name += ".txt"
    try:
        file = open(file_name, "r") # opens file in read-only mode
    except:
        print('this file does not exist')
        pygame.quit()
    for index, line in enumerate(file):
        maptext.append([]) # adds new row
        for j in line:
            if not j == "\n":
                maptext[index].append(j)
    mapsize = len(maptext[0]) # size should be divisible by it
    map_part_size = int(size/mapsize) # size of each rect in the map
    print(maptext)


for i in range(mapsize): # this thing converts the text into a list or rects
    for j in range(mapsize): # colum
        target_x = i*map_part_size
        target_y = j*map_part_size
        if maptext[i][j] == "#":
            map.append(pygame.Rect(target_x, target_y, map_part_size, map_part_size)) # a rect at the target cords with a width and height of map_part_size


""" end map setup """

""" debug stuff """
block_surface = pygame.Surface((map_part_size, map_part_size)) # a debug square
block_surface.fill(white)
player_sprite = pygame.Surface((4,4))
player_sprite.fill(yellow)

"""end debug stuff"""

"""game setup"""
FOV = 90
RES = 2 # thickness of lines
scan_lines = size/RES # amount of times to iteriate

player = player1.Player(size/2,size/2,4,map)
raycaster = player1.Raycaster(map)
"""end game setup"""




"""main loop"""
while True:
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key in MOVEMENT_KEYBINDS:
                player.direction-=MOVEMENT_KEYBINDS[event.key][2] # turn rotation offset
                player.direction-=MOVEMENT_KEYBINDS[event.key][1] # turn rotation
                player.move(MOVEMENT_KEYBINDS[event.key][0]) # move
                player.direction+=MOVEMENT_KEYBINDS[event.key][2] # turn back rotation offset
    # debug rendering
    screen.fill(black)
    for block in map:
        screen.blit(block_surface, block)
    screen.blit(player_sprite, player.rect)
    # end debug rendering
                

                


    pygame.display.flip() # updates display
    clock.tick(60) # 60 fps
            

    
    #end event handler"""

"""end main loop""" # it thinks this is code ???
