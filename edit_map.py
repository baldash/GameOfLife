import ctypes
from map import *

last_pos = [-1,-1]

def save_map(map, file_name):
    coords = get_living_cells_coords(map)
    if len(coords) > 0:
        with open(f"{MAP_FILES_FOLDER}/{file_name}.bld", "w") as f:
            for coord in coords:
                f.write(f"{coord[1]} {coord[0]}\n")
    else:
        print("error: trying to save to empty file name") # use gui message box to display errors in the future

def update_clicked_cell(map):
    global last_pos
    mousePos = get_mouse_position()
    x = (int)(mousePos.x / CELL_SIZE)
    y = (int)(mousePos.y / CELL_SIZE)

    if  (x != last_pos[0] or y != last_pos[1]) and (0 <= y < len(map) and 0 <= x < len(map[y])):
        map[y][x] = not map[y][x]
        last_pos = [x,y]
    return map

def edit_map():
    game_map = create_map()
    file_name = ""
    file_name_box_shape = Rectangle(WINDOW_SIZE + (int)(MENU_SIZE / 2) - (int)(80 / 2), (int)(WINDOW_SIZE / 5), 80, 40)
    save_button_shape = Rectangle(WINDOW_SIZE + (int)(MENU_SIZE / 2) - (int)(80 / 2), (int)(WINDOW_SIZE / 4), 80, 40)
    back_button_shape = Rectangle(WINDOW_SIZE + (int)(MENU_SIZE / 2) - (int)(80 / 2), (int)(WINDOW_SIZE * 0.75), 80, 40)

    while not window_should_close():
        if is_mouse_button_down(MOUSE_BUTTON_LEFT):
            game_map = update_clicked_cell(game_map)
        
        char = get_char_pressed()
        key = get_key_pressed()
        if key == KEY_BACKSPACE:
                print("remove")
                file_name = file_name[:-1]
        while char > 0:
            if 32 <= char <= 125 and len(file_name) < 20: # we use this workaround because the text box gui element doesn't work properly in python
                file_name += chr(char)
            char = get_char_pressed()
        
        gui_text_box(file_name_box_shape, file_name, 20, True)
        if gui_button(save_button_shape, "Save"):
            save_map(game_map, file_name)
        elif gui_button(back_button_shape, "Back"):
            break
        begin_drawing()
        clear_background(BLACK)
        draw_cells(game_map)
        draw_grid()
        end_drawing()