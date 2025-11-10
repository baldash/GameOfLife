from pyray import *
from params import *
import game_of_life as gol

play_button_shape = Rectangle((int)(WINDOW_SIZE / 2) - 80 / 2, (int)(WINDOW_SIZE / 2) - 100, 80, 40)
edit_button_shape = Rectangle((int)(WINDOW_SIZE / 2) - 80 / 2, (int)(WINDOW_SIZE / 2), 80, 40)
exit_button_shape = Rectangle((int)(WINDOW_SIZE / 2) - 80 / 2, (int)(WINDOW_SIZE / 2) + 100, 80, 40)
exit = False

init_window(WINDOW_SIZE, WINDOW_SIZE, WINDOW_TITLE)
while not window_should_close() and not exit:
    begin_drawing()
    clear_background(BLACK)
    if gui_button(play_button_shape, "Play"):
        gol.play()
    elif gui_button(edit_button_shape, "Edit"):
        print("edit")
    elif gui_button(exit_button_shape, "Exit"):
        exit = True
    end_drawing()
close_window()