#honestly idk if i need to import Pin or not but im doing it just in case lol
from machine import Pin
from project.lib.led_light import Led_Light
from time import sleep, time

#set led light pin
led = Led_Light(5, flashing = True, debug = True)

print("testing on()")
led.on()
if led.value == 1:
    print("uhh idkk")
sleep(1)

print("testing off()")
led.off()
if led.value == 0:
    print("yes")
sleep(1)

print("testing toggle()")
led.toggle()


print("testing led_light_state")
print(f"LED is {led.led_light_state}")

print("testing flash()")
led.flash()
sleep(5)

