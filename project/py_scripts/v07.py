from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from time import sleep, time
from controller import TrafficLightSubsystem, PedestrianSubsystem


pedestrired = Led_Light(19, True, True)
pedestrigreen = Led_Light(17, False, True)

red = Led_Light(3, False, True)
amber = Led_Light(5, False, True)
green = Led_Light(6, False, True)

pedestrianbutton = Pedestrian_Button(22, True)

buzzer = Audio_Notification(27, True)

light = TrafficLightSubsystem(red, amber, green, True)
pedestrianlight = PedestrianSubsystem(pedestrired, pedestrigreen, True)
button = PedestrianSubsystem(pedestrianbutton, True)
audio = Audio_Notification(buzzer, True)


def SubsystemDryer():
    #testing traffic light system
    print("testing traffic light in 5 seconds")
    sleep(5)

    #red light test
    light.show_red()
    print("pass if - red ON, amber OFF, green OFF")
    sleep(10)

    #amber light test
    light.show_amber()
    print("pass if - red OFF, amber ON, green OFF")
    sleep(10)

    #green light test
    light.show_green()
    print("pass if - red OFF, amber OFF, green ON")
    sleep(10)
    
    print("testing the peasant- i mean pedestrian lights in the approximately the amount of time i spend waiting at the tempe station lights every morning (3 years)")
    sleep(5)

    pedestrianlight.show_stop()
    print("pedestrian red light on")
    sleep(10)

    pedestrianlight.show_walk()
    print("pedestrian green light on")
    sleep(10)

    pedestrianlight.show_warning()
    print("pedestrian red light flashing")
    sleep(10)

    print("testing the button in 5")
    sleep(5)

    button.is_button_pressed()
    print("shows button value")
    sleep(10)

    button.reset_button()
    print("resets the button")
    sleep(10)

    print("testing the audio in 5")
    sleep(5)

    audio.warning_on()
    print("there should be an annoying beep")
    sleep(5)
    audio.warning_off()
    print("should stop now")
    sleep(10)

SubsystemDryer()
print("we are being held hostage. please send food and water to C10. tell my family i love them.")