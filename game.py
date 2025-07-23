import pygame
from enum import Enum
from collections import namedtuple

point = namedtuple('Point', ['x','y'])
direction = Enum(
    Right = 1,
    Down = 2,
    Left = 3,
    Up = 4
)
cell_size = 20
width = 20*cell_size
Hight = 20*cell_size
window = pygame.display.set_mode((width,Hight))