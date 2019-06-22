from time import sleep
import array
import subprocess

import config
from config import joy
from config import height, mode
from config import algos


def fmtFloat(n):
    return '{:6.3f}'.format(n)

def findLeftRegion():
    leftX, leftY = joy.leftStick()
    print(chr(27) + "[2J")
    print("X-Axis: ", leftX)
    print("Y-Axis: ", leftY)
    print(height)
    print(mode)
    sleep(.125)

# Called to have turtle begin startup routine
def bootup():
    config.init()
    setHeight(height)
    # subprocess.call(["xboxdrv","--led 1"])#,"--detach-kernel-driver"])

# Called to have turtle lay on belly
def shutdown():
    algos.run("shutdown")

# Called to set the turtle's operating height
def setHeight(heightValue):
    if heightValue == 0:
        algos.run("set_low_height")
    elif heightValue == 1:
        algos.run("set_reg_height")
    elif heightValue == 2:
        algos.run("standup")
        sleep(.5)
        algos.run("set_max_height")

while not joy.connected():
    sleep(1)

bootup()
while joy.connected():
    # This shuts down the turtle
    if joy.Back():
        break
    elif joy.Start():
        algos.run("standup")
        
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
    elif joy.A():
        continue
    elif joy.X():
        continue
    elif joy.B():
        continue
    elif joy.Y():
        continue

    findLeftRegion()
joy.close()

shutdown()