from req_libraries.Adafruit_PWM_Servo_Driver import PWM
from req_libraries.xbox import Joystick
from leg import Leg

### KEEPING FOR REF ###
#servo0 = 150  # 0 degrees Min pulse length out of 4096
#servo15 = 188 # 15 degrees
#servo30 = 225 # 30 degrees
#servo45 = 263 # 45 degrees
#servo60 = 300 # 60 degrees
#servo75 = 338 # 75 degrees
#servo90 = 375 # 90 degrees
#servo105 = 413 # 105 degrees
#servo120 = 450 # 105 degrees
#servo135 = 488 # 135 degrees
#servo150 = 525 # 150 degrees
#servo165 = 563 # 165 degrees
#servo180 = 625  # 180 degrees Max pulse length out of 4096
#servoStep = 38 # change by 15 degrees

pwm = PWM(0x40)
pwm.setPWMFreq(60) # Set frequency to 60 Hz
joy = Joystick()

height = 1
mode = 0

# Maps servo to position of PWM pins
fl1 =  0
fl2 =  1
fl3 =  2
bl1 =  3
bl2 =  4
bl3 =  5
br1 =  6
br2 =  7
br3 =  8
fr1 =  9
fr2 = 10
fr3 = 11

heightDirections = [1, 1, -1]
heightAngles = [30, 0, 90]

frontLeftLeg = Leg(fl1, fl2, fl3, True)
frontRightLeg = Leg(fr1, fr2, fr3, False)
backLeftLeg = Leg(bl1, bl2, bl3, True)
backRightLeg = Leg(br1, br2, br3, False)


def init():
    print "Test"
    #tweekValues()

#def tweekValues():
    #frontLeftLeg.tweekValue(2, 180, 640)
    #frontRightLeg.tweekValue(2, 180, 675)
    #backRightLeg.tweekValue(2, 180, 680)

    #frontLeftLeg.tweekValue(3, 180, 640)
    #frontRightLeg.tweekValue(3, 180, 640)
    #frontRightLeg.tweekValue(3, 30, 255)

    #backLeftLeg.tweekValue(3, 180, 600)
    #backLeftLeg.tweekValue(3, 150, 475)

    #servo[bl3] = servo[bl3][::-1]

def moveServo(servoNumber, degreeValue):
    if degreeValue == 0:  # Exits function if the degree value is not valid
        return False
    pwm.setPWM(servoNumber, 0, degreeValue)
    return True
