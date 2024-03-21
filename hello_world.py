#Imports
from microbit import *
import radio

display.show("hello world!") #Displays a string, character by character
sleep(500) #waits for 500ms
display.clear() #clears screan
display.show(123)#displays an integer
sleep(500)
display.scroll("Hello museum!") #Displays a string, but the text scrolls by
display.show(Image('00300:' #Sets brightness of each individual LED light, 0 - off, 9 - full brightness 
                   '03630:'
                   '36963:'
                   '03630:'
                   '00300'))
sleep(600)
display.clear()
