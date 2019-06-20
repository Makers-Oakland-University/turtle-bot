import time
import array
import subprocess

import config
from config import pwm, joy
from config import height, mode
from config import heightDirections, heightAngles
from config import frontLeftLeg, frontRightLeg, backLeftLeg, backRightLeg


def fmtFloat(n):
    return '{:6.3f}'.format(n)

def findLeftRegion():
    leftX, leftY = joy.leftStick()
    print(chr(27) + "[2J")
    print("X-Axis: ", leftX)
    print("Y-Axis: ", leftY)
    print(height)
    print(mode)
    time.sleep(.125)

def moveServo(servoNumber, degreeValue):
    if degreeValue == 0:  # Exits function if the degree value is not valid
        return False
    pwm.setPWM(servoNumber, 0, degreeValue)
    return True

# Called to have turtle begin startup routine
def bootup():
    config.init()
    setHeight(height)
    # subprocess.call(["xboxdrv","--led 1"])#,"--detach-kernel-driver"])

# Called to have turtle lay on belly
def shutdown():
    frontLeftLeg.move(0, 90, 45)
    frontRightLeg.move(0, 90, 45)
    backLeftLeg.move(0, 90, 45)
    backRightLeg.move(0, 90, 45)

# Called to set the turtle's operating height
def setHeight(heightValue):
    if heightValue == 0:
        frontLeftLeg.move(0, 30, 30)
        frontRightLeg.move(0, 30, 30)
        backLeftLeg.move(0, 30, 30)
        backRightLeg.move(0, 30, 30)
    elif heightValue == 1:
        frontLeftLeg.move(0, 0, -90)
        frontRightLeg.move(0, 0, -90)
        backLeftLeg.move(0, 0, -90)
        backRightLeg.move(0, 0, -90)
    elif heightValue == 2:
        standup()
        frontLeftLeg.move(0, -90, -90)
        frontRightLeg.move(0, -90, -90)
        backLeftLeg.move(0, -90, -90)
        backRightLeg.move(0, -90, -90)

def standup():
    frontLeftLeg.move(0, 75, 75)
    frontRightLeg.move(0, 75, 75)
    backLeftLeg.move(0, 75, 75)
    backRightLeg.move(0, 75, 75)
    time.sleep(.15)
    frontLeftLeg.move(0, -30, 0)
    frontRightLeg.move(0, -30, 0)
    backLeftLeg.move(0, -30, 0)
    backRightLeg.move(0, -30, 0)
    time.sleep(.15)
    frontLeftLeg.move(0, 0, -15)
    frontRightLeg.move(0, 0, -15)
    backLeftLeg.move(0, 0, -15)
    backRightLeg.move(0, 0, -15)
    time.sleep(.15)
    frontLeftLeg.move(0, -60, -60)
    frontRightLeg.move(0, -60, -60)
    backLeftLeg.move(0, -60, -60)
    backRightLeg.move(0, -60, -60)
    time.sleep(.2)
    frontLeftLeg.move(0, -90, 0)
    frontRightLeg.move(0, -90, 0)
    backLeftLeg.move(0, -90, 0)
    backRightLeg.move(0, -90, 0)
    time.sleep(.125)

while not joy.connected():
    time.sleep(1)

bootup()
while joy.connected():
    # This shuts down the turtle
    if joy.Back():
        break
    elif joy.Start():
        standup()

    elif joy.leftY() == 1:
        continue
    elif joy.leftY() == -1:
        continue
    elif joy.rightX() == 1:
        continue
    elif joy.rightX() == -1:
        continue

    # These change the working height of the turtle
    elif joy.dpadLeft():
        if height == 1:
            continue
        height = 1
        setHeight(height)
    elif joy.dpadRight():
        if height == 1:
            continue
        height = 1
        setHeight(height)
    elif joy.dpadUp():
        if height == 2:
            continue
        height = 2
        setHeight(height)
    elif joy.dpadDown():
        if height == 0:
            continue
        height = 0
        setHeight(height)

    elif joy.leftBumper():
        if mode != 0:
            mode -= 1
            while joy.leftBumper():
                time.sleep(.1)
    elif joy.rightBumper():
        if mode != 4:
            mode += 1
            while joy.rightBumper():
                time.sleep(.1)

    # The face buttons are currently used for testing purposes
    elif joy.X():
        continue
    elif joy.A():
        continue
    elif joy.B():
        continue
    elif joy.Y():
        continue

    findLeftRegion()
joy.close()

shutdown()