import numpy as np
from pyray import *
from params import *

def create_map():
    game_map = np.empty(shape=(CELL_NB, CELL_NB))
    game_map.fill(False)
    return game_map

def color_cell(x, y, color=WHITE):
    draw_rectangle(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE, color)

def get_living_cells_coords(game_map):
    return np.transpose(np.nonzero(game_map == True))

def draw_cells(map):
    cells = get_living_cells_coords(map)
    for cell in cells:
        color_cell(cell[1], cell[0])

def draw_grid():
    for y in range(0, CELL_NB):
        for x in range(0, CELL_NB):
            rec = Rectangle(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            draw_rectangle_lines_ex(rec, GRID_THICKNESS, GRAY)