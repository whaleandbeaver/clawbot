from vex import *

brain=Brain()
controller = Controller()
R1 = Motor(Ports.PORT1, True)
R2 = Motor(Ports.PORT2)
R3 = Motor(Ports.PORT3)
L1 = Motor(Ports.PORT4)
L2 = Motor(Ports.PORT5, True)
L3 = Motor(Ports.PORT6, True)
IN = Motor(Ports.PORT7, True)
EL = Motor(Ports.PORT8,)
SP1 = DigitalOut(brain.three_wire_port.a)
SP2 = DigitalOut(brain.three_wire_port.b)

def Control():

    piston = False
    elevate = False
    while True:

        lft = controller.axis2.position()
        rght = controller.axis3.position()

        L1.spin(FORWARD, lft)
        L2.spin(FORWARD, lft)
        L3.spin(FORWARD, lft)
        R1.spin(FORWARD, rght)
        R2.spin(FORWARD, rght)
        R3.spin(FORWARD, rght)


        if controller.buttonR2.pressing():
            IN.spin(REVERSE, 100)
            EL.spin(REVERSE, 100)
        
        if controller.buttonR1.pressing() and elevate == False:
            IN.stop()
            EL.stop()
            elevate = True

        if controller.buttonR1.pressing() and elevate == True:
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



Control()

