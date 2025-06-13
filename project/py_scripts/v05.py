from machine import Pin
from pedestrian_button import Pedestrian_Button
from time import ticks_ms, ticks_diff

button = Pin(22, Pin.IN, Pin.PULL_UP)

print("testing button_state")
button.button_state()

print("testing callback()")
button.callback()