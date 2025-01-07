from vex import *

brain=Brain()
controller = Controller()
R1 = Motor(Ports.PORT1)
R2 = Motor(Ports.PORT2, True)
R3 = Motor(Ports.PORT3, True)
L1 = Motor(Ports.PORT4, True)
L2 = Motor(Ports.PORT5)
L3 = Motor(Ports.PORT6)
mgr = MotorGroup(R1, R2, R3)
mgl = MotorGroup(L1, L2, L3)
drv = DriveTrain(mgl, mgr, 220, 400, 320)
IN = Motor(Ports.PORT7, True)
EL = Motor(Ports.PORT8,)
SP1 = DigitalOut(brain.three_wire_port.a)
SP2 = DigitalOut(brain.three_wire_port.b)
CL1 = DigitalOut(brain.three_wire_port.c)

def auto():
    SP1.set(False)
    SP2.set(True)
    drv.drive_for(REVERSE, 260, MM)
    SP1.set(True)
    SP2.set(False)
    IN.spin(FORWARD, 100)
    EL.spin(FORWARD, 100)
#    drv.turn_for(RIGHT, 6, DEGREES)
    

def control():

    piston = False
    pistonc = False
    elevate = True
    while True:

        lft = controller.axis3.position()
        rght = controller.axis2.position()
        mgl.spin(FORWARD, lft)
        mgr.spin(FORWARD, rght)

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

        if controller.buttonUp.pressing() and pistonc == False:
            while controller.buttonUp.pressing():
                CL1.set(True)
                pistonc = True

        if controller.buttonUp.pressing() and pistonc == True:
            while controller.buttonUp.pressing():
                CL1.set(False)
                pistonc = False

while True:
    if controller.buttonA.pressing():
        auto()
        control()
        break

    if controller.buttonB.pressing():
        control()
        break