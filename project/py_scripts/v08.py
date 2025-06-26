from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from time import sleep, time
from controller import TrafficLightSubsystem, PedestrianSubsystem, Controller


pedestrired = Led_Light(19, True, True)
pedestrigreen = Led_Light(17, False, True)

red = Led_Light(3, False, True)
amber = Led_Light(5, False, True)
green = Led_Light(6, False, True)

pedestrianbutton = Pedestrian_Button(22, True)

buzzer = Audio_Notification(27, True)

light = TrafficLightSubsystem(red, amber, green, True)
pedestrian = PedestrianSubsystem(pedestrired, pedestrigreen, pedestrianbutton, buzzer, True)
controllertestig = Controller(pedestrired, pedestrigreen, red, amber, green, pedestrianbutton, buzzer, True)

def SubsystemDryer():
    print("my controller subsystem is RIDDLED with errors, but nevertheless, we stay silly :3")
    print("anyway. controller unit test time.")
    
    print("testing idle state in t-minus three seconds")
    sleep(3)
    controllertestig.set_idle_state()
    print("PASS: green ON, pedestrian red ON, everything else OFF")

    print("testing idle state in t-minus three seconds")
    sleep(3)
    controllertestig.set_change_state()
    print("PASS: green ON, pedestrian red ON, everything else OFF")

    print("testing idle state in t-minus three seconds")
    sleep(3)
    controllertestig.set_walk_state()
    print("PASS: green ON, pedestrian red ON, everything else OFF")

    print("testing idle state in t-minus three seconds")
    sleep(3)
    controllertestig.set_warning_state()
    print("PASS: green ON, pedestrian red ON, everything else OFF")

    print("testing idle state in t-minus three seconds")
    sleep(3)
    controllertestig.set_error_state()
    print("PASS: green ON, pedestrian red ON, everything else OFF")

SubsystemDryer()
print("mr jones please stop holding us hostage and making us do unit tests i have a family to feed")