# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Created:      8/7/2024, 4:41:29 PM                                         #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #


#Defining

from vex import *

brain=Brain()
LM = Motor(Ports.PORT1)
RM = Motor(Ports.PORT2, True)
UP = Motor(Ports.PORT3)
CLAW = Motor(Ports.PORT4)
controller = Controller()
Dtrain = DriveTrain(LM, RM, 314, 300, 165)

#All robot functions

def Up():
    UP.spin(FORWARD, 75)

def Down():
    UP.spin(REVERSE, 75)

def Stop():
    UP.set_stopping(HOLD)
    UP.stop()


def Close():
    CLAW.spin(FORWARD, 75)

def Open():
    CLAW.spin(REVERSE, 75)

def CStop():
    CLAW.set_stopping(HOLD)
    CLAW.stop()

#Function activation keys

def control_robot():

    controller.buttonR1.pressed(Up)
    controller.buttonR1.released(Stop)
    controller.buttonR2.pressed(Down)
    controller.buttonR2.released(Stop)

    controller.buttonL1.pressed(Close)
    controller.buttonL1.released(CStop)
    controller.buttonL2.pressed(Open)
    controller.buttonL2.released(CStop)

    controller.buttonUp.pressed(Open)
    controller.buttonUp.released(CStop)
    controller.buttonDown.pressed(Close)
    controller.buttonDown.released(CStop)
    controller.buttonY.pressed(DRAW2)

#Driving 

    while True:

        left_x = controller.axis3.position()
        left_y = controller.axis2.position()
        
        LM.spin(FORWARD, left_x)
        RM.spin(FORWARD, left_y)

def pre_auto():

    UP.spin(FORWARD, 100)
    CLAW.spin(FORWARD, 100)
    wait(200)
    CStop()
    wait(1100)
    Stop()
    RM.spin(FORWARD, 25)
    wait(5900)
    RM.stop()
    Dtrain.drive_for(FORWARD, 11)
    UP.spin(REVERSE, 50)
    wait(1000)
    Stop()

    control_robot()

#PARTY DISTRICT

def Draw():
    brain.screen.set_pen_color(Color.WHITE)
    brain.screen.set_pen_width(2)
    brain.screen.draw_line(70, 50, 130, 50)
    brain.screen.draw_line(170, 50, 230, 50)
    brain.screen.draw_circle(100, 100, 30)
    brain.screen.draw_circle(200, 100, 30)

    brain.screen.draw_line(70, 100, 130, 100)
    brain.screen.draw_line(170, 100, 230, 100)
    brain.screen.draw_line(100, 130, 100, 70)
    brain.screen.draw_line(200, 70, 200, 130)

    brain.screen.draw_rectangle(100, 175, 100, 25)
    brain.screen.draw_line(125, 175, 125, 200)
    brain.screen.draw_line(150, 175, 150, 200)
    brain.screen.draw_line(175, 175, 175, 200)

    brain.screen.set_fill_color(Color.BLACK)
    brain.screen.draw_circle(100, 100, 10)
    brain.screen.draw_circle(200, 100, 10)

def DRAW2():
    brain.screen.print("Testbot: Built by titus, modified by Jeffery")
    brain.screen.set_cursor(3, 30)
    brain.screen.print("coded by Isadore")

    while True:
        brain.screen.clear_screen
        brain.screen.set_fill_color(Color.RED)
        Draw()
        wait(50)
        brain.screen.clear_screen
        brain.screen.set_fill_color(Color.GREEN)
        Draw()
        wait(50)
        brain.screen.clear_screen
        brain.screen.set_fill_color(Color.ORANGE)
        Draw()
        wait(50)
        brain.screen.clear_screen
        brain.screen.set_fill_color(Color.BLUE)
        Draw()
        wait(50)
        brain.screen.clear_screen
        brain.screen.set_fill_color(Color.PURPLE)
        Draw()
        wait(50)
        brain.screen.clear_screen
        brain.screen.set_fill_color(Color.YELLOW)
        Draw()
        wait(50)

while True:
    if controller.buttonA.pressing():
        pre_auto()
        break

    if controller.buttonB.pressing():
        control_robot()
        break