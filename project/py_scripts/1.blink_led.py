from machine import pin
from time import sleep

sleep(0.1)

led_pin = 25

led = Pin(led_pin, Pin.OUT)

while True:
    led.value(True)
    sleep(1)
    led.value(False)
    sleep(1)