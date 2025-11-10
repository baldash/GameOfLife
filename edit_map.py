from map import *

def save_map(map):
    coords = get_living_cells_coords(map)
    if len(coords) > 0:
        with open(f"{MAP_FILES_FOLDER}/test.bld", "w") as f:
            for coord in coords:
                f.write(f"{coord[1]} {coord[0]}\n")

def update_clicked_cell(map):
    mousePos = get_mouse_position()
    x = (int)(mousePos.x / CELL_SIZE)
    y = (int)(mousePos.y / CELL_SIZE)

    if (0 <= y < len(map) and 0 <= x < len(map[y])):
        map[y][x] = True
    return map

def edit_map():
    game_map = create_map()
    save_button_shape = Rectangle(WINDOW_SIZE + (int)(MENU_SIZE / 2) - (int)(80 / 2), (int)(WINDOW_SIZE / 4), 80, 40)
    back_button_shape = Rectangle(WINDOW_SIZE + (int)(MENU_SIZE / 2) - (int)(80 / 2), (int)(WINDOW_SIZE * 0.75), 80, 40)

    while not window_should_close():
        if is_mouse_button_down(MOUSE_BUTTON_LEFT):
            game_map = update_clicked_cell(game_map)
        if gui_button(save_button_shape, "Save"):
            save_map(game_map)
        elif gui_button(back_button_shape, "Back"):
            break
        begin_drawing()
        clear_background(BLACK)
        draw_cells(game_map)
        draw_grid()
        end_drawing()