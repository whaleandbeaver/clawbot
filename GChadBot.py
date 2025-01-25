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
CL2 = DigitalOut(brain.three_wire_port.d)

def auto():
    drv.set_drive_velocity(50)
    SP1.set(False)
    SP2.set(True)
    drv.drive_for(REVERSE, 260, MM)
    SP1.set(True)
    SP2.set(False)
    IN.spin(FORWARD, 100)
    EL.spin(FORWARD, 100)
    wait(2000, MSEC)
    mgl.spin_for(FORWARD, 360, DEGREES, 25, PERCENT)
    drv.drive_for(FORWARD, 130, MM)
    wait(3000, MSEC)
    drv.drive_for(REVERSE, 130, MM)
    mgl.spin_for(REVERSE, 320, DEGREES, 25, PERCENT)
    drv.drive_for(REVERSE, 250, MM)
    

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
                CL1.set(True)
                pistonc = True

        if controller.buttonUp.pressing() and pistonc == True:
            while controller.buttonUp.pressing():
                CL1.set(False)
                CL1.set(False)
                pistonc = False

comp = Competition(control, auto)