# Imports for microbit and radio 
from microbit import *
import radio

#set radio group
radio.config(group=1)

#turn on the radio
radio.on()

MESSAGE = "Hello, muzej!" #max 19 ASCII characters

while True:
    #sends a radio message when button A is pressed
    if button_a.is_pressed(): 
        radio.send(MESSAGE)

    #displays radio message when microbit recieves it
    radio_message = radio.receive()
    if radio_message:
        display.scroll(radio_message)
