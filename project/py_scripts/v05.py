from machine import Pin
from pedestrian_button import Pedestrian_Button
from time import ticks_ms, ticks_diff

button = Pin(22, Pin.IN, Pin.PULL_UP, debug = True)

print("testing button_state")
button.button_state()
print("i think this worked idk how to do unit tests")
sleep(0.1)

print("testing callback()")
button.callback()
print(current_time)
print("uhhhh")
print("i think this works?")