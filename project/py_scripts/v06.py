from machine import Pin
from time import sleep, time
from audio_notification import Audio_Notification

buzzer = machine.PWM(27)

print("testing beep()")
buzzer.beep()

print("testing warning_on()")
buzzer.warning_on()

print("testing warning_off()")
buzzer.warning_off()