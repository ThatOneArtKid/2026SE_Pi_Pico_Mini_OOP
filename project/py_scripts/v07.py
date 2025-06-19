from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from time import sleep, time
from controller import TrafficLightSubsystem, PedestrianSubsystem


led_pedestrian_red = Led_Light(19, True, True)
led_pedestrian_green = Led_Light(17, False, True)
led_car_red = Led_Light(3, False, True)
led_car_amber = Led_Light(5, False, True)
led_car_green = Led_Light(7, False, True)
pedestrianbutton = Pedestrian_Button(22, True)
buzzer = Audio_Notification(27, True)

def SubsystemDryer():
    #yes

SubsystemDryer()