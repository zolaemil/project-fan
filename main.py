def on_button_pressed_a():
    global duty
    duty = min(duty + 1, 5)
    pins.analog_write_pin(AnalogPin.P0, duty * 200)
    basic.show_number(duty)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    music.play(music.string_playable("- - B - B - B - ", 300),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("C5 C5 B A - G - G ", 300),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("E - G D D D - - ", 300),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global duty
    duty = max(duty - 1, 0)
    pins.analog_write_pin(AnalogPin.P0, duty * 200)
    basic.show_number(duty)
input.on_button_pressed(Button.B, on_button_pressed_b)

duty = 0
duty = 0
basic.show_number(duty)