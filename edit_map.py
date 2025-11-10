from map import *

def update_clicked_cell(map):
    mousePos = get_mouse_position()
    x = (int)(mousePos.x / CELL_SIZE)
    y = (int)(mousePos.y / CELL_SIZE)

    if (0 <= y < len(map) and 0 <= x < len(map[y])):
        map[y][x] = True
    return map

def edit_map():
    game_map = create_map()

    while not window_should_close():
        if is_mouse_button_down(MOUSE_BUTTON_LEFT):
            game_map = update_clicked_cell(game_map)
        begin_drawing()
        clear_background(BLACK)
        draw_cells(game_map)
        draw_grid()
        end_drawing()