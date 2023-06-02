import pygame
from setting import *
from maze import Maze
from tiles import Tile

pygame.init()

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
maze = Maze(maze_matrix, SCREEN)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic and drawing code goes here
    test_tile = Tile((0, 0), tile_size)
    SCREEN.fill('black')
    maze.run()
    pygame.display.update()

pygame.quit()
