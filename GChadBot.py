from vex import *

brain=Brain()
controller = Controller()
R1 = Motor(Ports.PORT1)
R2 = Motor(Ports.PORT2, True)
R3 = Motor(Ports.PORT3, True)
L1 = Motor(Ports.PORT4, True)
L2 = Motor(Ports.PORT5)
L3 = Motor(Ports.PORT6)
IN = Motor(Ports.PORT7, True)
EL = Motor(Ports.PORT8,)
SP1 = DigitalOut(brain.three_wire_port.a)
SP2 = DigitalOut(brain.three_wire_port.b)

def autonomous():
    L1.spin(FORWARD, 100)
    L2.spin(FORWARD, 100)
    L3.spin(FORWARD, 100)
    R1.spin(FORWARD, 100)
    R2.spin(FORWARD, 100)
    R3.spin(FORWARD, 100)
    wait(5000)
    L1.stop()
    L2.stop()
    L3.stop()
    R1.stop()
    R2.stop()
    R3.stop()

def user_control():

    piston = False
    elevate = True
    while True:

        lft = controller.axis2.position()
        rght = controller.axis3.position()

        L1.spin(FORWARD, lft)
        L2.spin(FORWARD, lft)
        L3.spin(FORWARD, lft)
        R1.spin(FORWARD, rght)
        R2.spin(FORWARD, rght)
        R3.spin(FORWARD, rght)

 
        if controller.buttonR2.pressing() and elevate == True:
            while controller.buttonR2.pressing():
                IN.spin(REVERSE, 100)
                EL.spin(REVERSE, 100)
                elevate = False

        if controller.buttonR2.pressing() and elevate == False:
            while controller.buttonR2.pressing():
                IN.stop()
                EL.stop()
                elevate = True
        
        if controller.buttonR1.pressing() and elevate == False:
            while controller.buttonR1.pressing():
                IN.stop()
                EL.stop()
                elevate = True

        if controller.buttonR1.pressing() and elevate == True:
            while controller.buttonR1.pressing():
                IN.spin(FORWARD, 100)
                EL.spin(FORWARD, 100)
                elevate = False

        if controller.buttonA.pressing() and piston == False:
            while controller.buttonA.pressing():
                SP1.set(True)
                SP2.set(False)
                piston = True

        if controller.buttonA.pressing() and piston == True:
            while controller.buttonA.pressing():
                SP1.set(False)
                SP2.set(True)
                piston = False



user_control()

comp = Competition(user_control, autonomous)