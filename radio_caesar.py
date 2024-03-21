# Imports for microbit and radio 
from microbit import *
import radio

MESSAGE = "dober dan" #max 19 ASCII characters
OFFSET_KEY = 2 #key used for the caesar cypher

#set radio group
radio.config(group=1)

#turn on the radio
radio.on()

#caesers cypher, works only on the english alphabeth character
def caesar_cypher(text, offset):
    text = text.lower() #set text to lowercase for simplicity
    answer = ""
    for character in text:
        if character == " ": #keep the spaces
            answer += " "
        else:
            answer += chr((ord(character) + offset - 97) % 26 + 97) #move the letter for the offset
    return answer

#function for decyphering caesar cypher 
def caesar_decypher(text, offset):
    answer = ""
    for character in text:
            if character == " ":
                answer += " "
            else:
                answer += chr((ord(character) - offset - 97) % 26 + 97)

    return answer

while True:
        #sends a message when button A is pressed
        if button_a.is_pressed(): 
            radio.send(caesar_cypher(MESSAGE, OFFSET_KEY))
        radio_message = radio.receive()
        #decyphers and displays message when it is recieved
        if radio_message:
            display.scroll(caesar_decypher(radio_message, OFFSET_KEY))
