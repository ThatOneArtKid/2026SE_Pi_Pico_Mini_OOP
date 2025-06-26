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
pedestrian = PedestrianSubsystem(pedestrired, pedestrigreen, pedestrianbutton, buzzer, True)

def SubsystemDryer():
    #testing controller FIRST because i am not waiting for all that

    #testing traffic light system
    print("testing traffic light in 5 seconds")
    sleep(3)

    #red light test
    light.show_red()
    print("pass if - red ON, amber OFF, green OFF")
    sleep(3)

    #amber light test
    light.show_amber()
    print("pass if - red OFF, amber ON, green OFF")
    sleep(3)

    #green light test
    light.show_green()
    print("pass if - red OFF, amber OFF, green ON")
    sleep(1)
    
    print("testing the peasant- i mean pedestrian lights in the approximately the amount of time i spend waiting at the tempe station lights every morning (3 years)")
    sleep(2)

    pedestrian.show_stop()
    print("pedestrian red light on")
    sleep(3)

    pedestrian.show_walk()
    print("pedestrian green light on")
    sleep(3)

    pedestrian.show_warning()
    print("pedestrian red light flashing")
    sleep(3)

    print("testing the button in 5")
    sleep(3)

    pedestrian.is_button_pressed()
    print("shows button value")
    sleep(3)

    pedestrian.reset_button()
    print("resets the button")
    sleep(3)

    print("testing the audio in 5")
    sleep(3)

    pedestrian.warning_on()
    print("there should be an annoying beep")
    sleep(3)
    pedestrian.warning_off()
    print("should stop now")
    sleep(3)

SubsystemDryer()
print("we are being held hostage. please send food and water to C10. tell my family i love them.")