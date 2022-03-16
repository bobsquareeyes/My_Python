                                                                                                                                                                                                                      #!/usr/bin/python3
#Imports ------------------------------------------------------------
from buildhat import Motor
from guizero import App, Slider, PushButton
#Definitions -------------------------------------------------------
motor_a = Motor("A")
motor_b = Motor("B")
speed = 25
speed2 = -25
def on_button():
     motor_a.start(speed=speed)
     motor_b.start(speed=speed2)
def off_button():
     motor_a.stop()
     motor_b.stop()
def update_speed():
     off_button()
     on_button()
def update_speed_var():
     global speed
     global speed2
     speed = speed_control.value
     speed2 = speed_control.value * -1
     #speed2 = speed
def exitprogram():
     off_button()
     app.destroy()
#Gui ---------------------------------------------------------------
app = App("Fan Controller")
speed_control = Slider(app, start=-100, end=100, command=update_speed_var)
Off = PushButton(app, text="Turn off fans.", command=off_button)
Update = PushButton(app, text="Update fans speed/Start fans.", command=update_speed)
Exit = PushButton(app, text="Exit the program.", command=exitprogram)
app.display()
