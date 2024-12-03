from vex import *

brain=Brain()
controller = Controller()
L1 = Motor(Ports.PORT1, True)
L2 = Motor(Ports.PORT2)
L3 = Motor(Ports.PORT3)
R1 = Motor(Ports.PORT4)
R2 = Motor(Ports.PORT5, True)
R3 = Motor(Ports.PORT6, True)
IN = Motor(Ports.PORT7, GearSetting.RATIO_6_1, True)
EL = Motor(Ports.PORT8, GearSetting.RATIO_6_1)
SP1 = DigitalOut(brain.three_wire_port.a)
SP2 = DigitalOut(brain.three_wire_port.b)

def Control():

    piston = False
    while True:

        lft = controller.axis3.position()
        rght = controller.axis2.position()

        L1.spin(FORWARD, lft)
        L2.spin(FORWARD, lft)
        L3.spin(FORWARD, lft)
        R1.spin(FORWARD, rght)
        R2.spin(FORWARD, rght)
        R3.spin(FORWARD, rght)

        if controller.buttonR1.pressing():
            IN.spin(FORWARD, 100)
            EL.spin(FORWARD, 100)
        else:

            if controller.buttonR2.pressing():
                IN.spin(REVERSE, 100)
                EL.spin(REVERSE, 100)
            else:
                IN.stop()
                EL.stop()

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