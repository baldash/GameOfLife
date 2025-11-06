from pyray import *
from params import *
import numpy as np

def load_cells():
    cells = []
    with open(INIT_FILE, 'r') as file:
        for line in file:
            print(line.strip())
            if ("#" not in line):
                splitted_coords = line.split()
                cells.append([(int)(splitted_coords[0]), (int)(splitted_coords[1])])
    
    return cells

def create_map():
    global CELL_NB
    game_map = np.empty(shape=(CELL_NB, CELL_NB))
    game_map.fill(False)
    return game_map

def update_map(game_map, cells):
    for cell in cells:
        game_map[cell[1]][cell[0]] = True
    return game_map

def get_living_cells_coords(game_map):
    return np.transpose(np.nonzero(game_map == True))

def color_cell(x, y, color=WHITE):
    draw_rectangle(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE, color)

def draw_cells(cells):
    for cell in cells:
        color_cell(cell[0], cell[1])

def draw_grid():
    global CELL_NB
    for y in range(0, CELL_NB):
        for x in range(0, CELL_NB):
            rec = Rectangle(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            draw_rectangle_lines_ex(rec, GRID_THICKNESS, GRAY)

def count_living_neigbours(x, y, cells):
    pass

def game_of_life(cells):
    neighbours = [
        [-1,-1], 
        [0, -1], 
        [1, -1], 
        [-1, 0], 
        [1, 0], 
        [-1, 1], 
        [0, 1], 
        [1, 1]
        ]
    
    return cells


CELL_NB = (int)(WINDOW_SIZE / CELL_SIZE)
cells = load_cells()
game_map = create_map()
game_map = update_map(game_map, cells)

last_update_time = 0

if (len(cells) > 0):
    init_window(WINDOW_SIZE, WINDOW_SIZE, WINDOW_TITLE)
    while not window_should_close():
        if ((int)(get_time()) - last_update_time == 2):
            last_update_time = (int)(get_time())
            # cells = game_of_life(cells)
        begin_drawing()
        clear_background(BLACK)
        draw_cells(cells)
        draw_grid()
        end_drawing()
    close_window()