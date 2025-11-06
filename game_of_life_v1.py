from pyray import *
from params import *

def color_cell(x, y, color=WHITE):
    draw_rectangle(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE, color)

init_window(WINDOW_SIZE, WINDOW_SIZE, WINDOW_TITLE)
while not window_should_close():
    begin_drawing()
    clear_background(BLACK)
    for y in range(0, (int)(WINDOW_SIZE / CELL_SIZE)):
        for x in range(0, (int)(WINDOW_SIZE / CELL_SIZE)):
            draw_rectangle_lines(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE, WHITE)
    color_cell(6, 2)
    end_drawing()
close_window()