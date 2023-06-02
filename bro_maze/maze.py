import pygame
from tiles import Tile
from setting import tile_size


class Maze:
    def __init__(self, level_data, surface):
        self.tiles = pygame.sprite.Group()
        self.setup_level(level_data)
        self.display_surface = surface

    def setup_level(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if col == 1:
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)

    def run(self):
        self.tiles.draw(self.display_surface)

