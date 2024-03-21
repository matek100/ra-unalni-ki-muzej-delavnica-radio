# Imports for microbit and radio 
from microbit import *
import radio
import os

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

#Brute force attack on caesr_cypher 
def brutus(text):
    for i in range(0, 26): #interate over all possible offsets
        display.scroll(caesar_decypher(text, i))
        #Wait until user presses a button
        while True:
            if button_a.is_pressed() or button_b.is_pressed():
                break
       #if button A is pressed devyphered text makes sense         
        if button_a.was_pressed():
            display.scroll("Key is: " + str(i))
            break
        #if button B is pressed continiue with the next possible offset
        if button_b.was_pressed():
            continue
        



while True:
        #sends a message when button A and B are pressed
        if button_a.is_pressed() and button_b.is_pressed(): 
            radio.send(caesar_cypher(MESSAGE, OFFSET_KEY))
        radio_message = radio.receive()
        #decyphers and displays message when it is recieved
        if radio_message:
            brutus(radio_message)
