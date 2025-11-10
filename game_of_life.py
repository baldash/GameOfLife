from pyray import *
from params import *
import numpy as np
import re
import sys
import glob

CELL_NB = (int)(WINDOW_SIZE / CELL_SIZE)

def load_cells():
    cells = []
    pattern = re.compile("^\\d+\\s+\\d+\\s*$")
    line_nb = 1
    path = r'./'+ MAP_FILES_FOLDER + '/**/*.bld'
    files = glob.glob(path, recursive=True)

    for file in files:
        with open(file, 'r') as file:
            for line in file:
                if (line[0] != "#" and len(line.strip()) > 0):
                    if pattern.match(line):
                        splitted_coords = line.split()
                        cells.append([(int)(splitted_coords[0]), (int)(splitted_coords[1])])
                    else:
                        print(f"error in file {file} at line {line_nb}:\n>>> {line}", file=sys.stderr)
                line_nb += 1
    
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

def draw_cells(map):
    cells = get_living_cells_coords(map)
    for cell in cells:
        color_cell(cell[1], cell[0])

def draw_grid():
    global CELL_NB
    for y in range(0, CELL_NB):
        for x in range(0, CELL_NB):
            rec = Rectangle(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            draw_rectangle_lines_ex(rec, GRID_THICKNESS, GRAY)

def count_living_neigbours(x, y, map):
    global CELL_NB

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
    nb_neighbours = 0

    for neighbour in neighbours:
        if x + neighbour[0] > 0 and x + neighbour[0] < CELL_NB and y + neighbour[1] > 0 and y + neighbour[1] < CELL_NB:
            nb_neighbours += map[y + neighbour[1]][x + neighbour[0]] == True

    return nb_neighbours

def game_of_life(map):
    new_map = map.copy()
    
    for y in range(0, len(map)):
        for x in range(0, len(map[y])):
            nb_neighbours = count_living_neigbours(x, y, map)
            if nb_neighbours < 2:
                new_map[y][x] = False
            elif map[y][x] == True and nb_neighbours > 3:
                new_map[y][x] = False
            elif map[y][x] == False and nb_neighbours == 3:
                new_map[y][x] = True
    return new_map

def play():
    cells = load_cells()
    game_map = create_map()
    game_map = update_map(game_map, cells)

    last_update_time = 0

    if (len(cells) > 0):
        #init_window(WINDOW_SIZE, WINDOW_SIZE, WINDOW_TITLE)
        while not window_should_close():
            if (get_time() - last_update_time >= REFRESH_TIME):
                last_update_time = get_time()
                game_map = game_of_life(game_map)
            begin_drawing()
            clear_background(BLACK)
            draw_cells(game_map)
            draw_grid()
            end_drawing()