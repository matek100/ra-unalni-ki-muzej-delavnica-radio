radio.set_group(1) #define the radio group
MESSAGE = "Hello, muzej!" #max 19 ASCII characters

def on_button_pressed_a():
    radio.send_string(MESSAGE)

def on_received_string(receivedString):
    basic.show_string(receivedString)

input.on_button_pressed(Button.A, on_button_pressed_a) #when button A is pressed it calls function on_button_pressed_a
radio.on_received_string(on_received_string) #when string is recieved it calls function on_received_string
