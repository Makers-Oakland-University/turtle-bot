from Adafruit_PWM_Servo_Driver import PWM
import time
import xbox
import array
import subprocess

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

def fillDefaultArray(currArray):
  for x in range(0, 181):
    if x == 0:
      currArray.append(150)
    elif x == 15:
      currArray.append(188)
    elif x == 30:
      currArray.append(225)
    elif x == 45:
      currArray.append(263)
    elif x == 60:
      currArray.append(300)
    elif x == 75:
      currArray.append(338)
    elif x == 90:
      currArray.append(375)
    elif x == 105:
      currArray.append(413)
    elif x == 120:
      currArray.append(450)
    elif x == 135:  
      currArray.append(488)
    elif x == 150:
      currArray.append(525)
    elif x == 165:
      currArray.append(563)
    elif x == 180:
      currArray.append(650)
    else:
      currArray.append(0)

def setUpArrays():
  fillDefaultArray(servo1)
  fillDefaultArray(servo2)
  fillDefaultArray(servo3)
  fillDefaultArray(servo4)
  fillDefaultArray(servo5)
  fillDefaultArray(servo6)
  fillDefaultArray(servo7)
  fillDefaultArray(servo8)
  fillDefaultArray(servo9)
  fillDefaultArray(servo10)
  fillDefaultArray(servo11)
  fillDefaultArray(servo12)

def tweekValues():
  servo[fl1] = servo[fl1][::-1]
  servo[bl1] = servo[bl1][::-1]
  servo[fr1] = servo[fr1][::-1]
  servo[br1] = servo[br1][::-1]

  servo[fl2][180] = 640
  servo[fr2][180] = 675
  servo[br2][180] = 680

  servo[fl3][180] = 640
  servo[fr3][180] = 640
  servo[fr3][30] = 255

  servo[bl3][180] = 600
  servo[bl3][150] = 475

  servo[bl3] = servo[bl3][::-1]

pwm = PWM(0x40)
joy = xbox.Joystick()
pwm.setPWMFreq(60) # Set frequency to 60 Hz
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

# Arrays spicific to each servo holding thier respective PWM signals
servo1  = [] # Front Left 1
servo2  = [] # Front Left 2
servo3  = [] # Front Left 3
servo4  = [] # Back Left 1
servo5  = [] # Back Left 2
servo6  = [] # Back Left 3
servo7  = [] # Back Right 1
servo8  = [] # Back Right 2
servo9  = [] # Back Right 3
servo10 = [] # Front Right 1
servo11 = [] # Front Right 2
servo12 = [] # Front Right 3

heightDirections = [1, 1, -1]
heightAngles = [30, 0, 90]

# Master servo array, used for calling all child arrays
servo = [servo1, servo2, servo3, servo4, servo5, servo6, servo7, servo8, servo9, servo10, servo11, servo12]

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

# Called to have turtle begin startup routine
def bootup():
  setHeight(height)
  #subprocess.call(["xboxdrv","--led 1"])#,"--detach-kernel-driver"])

# Called to have turtle lay on belly
def shutdown():
  moveServo(fl1, 1, 0)
  moveServo(fl2, 1, 90)
  moveServo(fl3, 1, 45)

  moveServo(bl1, 1, 0)
  moveServo(bl2, 1, 90)
  moveServo(bl3, 1, 45)
  
  moveServo(fr1, 1, 0)
  moveServo(fr2, 1, 90)
  moveServo(fr3, 1, 45)

  moveServo(br1, 1, 0)
  moveServo(br2, 1, 90)
  moveServo(br3, 1, 45)

# Called to set the turtle's operating height
def setHeight(heightValue):
  moveServo(fl1, 1, 0)
  moveServo(bl1, 1, 0)
  moveServo(fr1, 1, 0)
  moveServo(br1, 1, 0)
  if heightValue == 0:
    moveServo(fl1, 1, 0)
    moveServo(fl2, 1, 30)
    moveServo(fl3, 1, 30)

    moveServo(bl2, 1, 30)
    moveServo(bl3, 1, 30)

    moveServo(fr2, 1, 30)
    moveServo(fr3, 1, 30)

    moveServo(br2, 1, 30)
    moveServo(br3, 1, 30) 
  elif heightValue == 1:
    moveServo(fl2, 1, 0)
    moveServo(fl3, 1, 0)
 
    moveServo(bl2, 1, 0)
    moveServo(bl3, 1, 0)

    moveServo(fr2, 1, 0)
    moveServo(fr3, 1, 0)

    moveServo(br2, 1, 0)
    moveServo(br3, 1, 0)
  elif heightValue == 2:
    standup()
    moveServo(fl2, -1, 90)
    moveServo(fl3, -1, 90)

    moveServo(bl2, -1, 90)
    moveServo(bl3, -1, 90)

    moveServo(fr2, -1, 90)
    moveServo(fr3, -1, 90)

    moveServo(br2, -1, 90)
    moveServo(br3, -1, 90)

# Direction should indicate '1' for forward and '-1' for backward
def moveServo(servoNumber, direction, degree):
  if (degree % 15 != 0 or degree > 90): # Exits function if the degree value is not valid
    return

  if (servoNumber < 5): # Occurs if the server is on the left side of the body
    if (direction > 0): # Indicates forward
      pwm.setPWM(servoNumber, 0, servo[servoNumber][90-degree])
    elif (direction < 0): # Indicates backward
      pwm.setPWM(servoNumber, 0, servo[servoNumber][90+degree])
  else: # Occurs if the server is on the right side of the body
    if (direction > 0): # Indicates forward
      pwm.setPWM(servoNumber, 0, servo[servoNumber][90+degree])
    elif (direction < 0): # Indicates backward
      pwm.setPWM(servoNumber, 0, servo[servoNumber][90-degree])    

def moveLegStraight(legID, legDirection, amountMoved, riseAmount, moveNow):
  temp1 =  heightAngles[height] * heightDirections[height]
  temp2 = temp1 + riseAmount
  if temp2 < 0:
    dir = -1
  else:
    dir = 1
  if legID == "fl":
    moveServo(fl2, dir, abs(temp2))
    moveServo(fl3, dir, abs(temp2))
    time.sleep(.125)
    moveServo(fl1, legDirection, amountMoved)
    time.sleep(.15)
    moveServo(fl2, heightDirections[height], heightAngles[height])
    moveServo(fl3, heightDirections[height], heightAngles[height])
    time.sleep(.125)
    if moveNow:
      moveServo(fl1, 1, 0)
      time.sleep(.15)
  elif legID == "fr":
    moveServo(fr2, dir, abs(temp2))
    moveServo(fr3, dir, abs(temp2))
    time.sleep(.125)
    moveServo(fr1, legDirection, amountMoved)
    time.sleep(.15)
    moveServo(fr2, heightDirections[height], heightAngles[height])
    moveServo(fr3, heightDirections[height], heightAngles[height])
    time.sleep(.125)
    if moveNow:
      moveServo(fr1, 1, 0)
      time.sleep(.15)
  elif legID == "bl":
    moveServo(bl2, dir, abs(temp2))
    moveServo(bl3, dir, abs(temp2))
    time.sleep(.125)
    moveServo(bl1, legDirection, amountMoved)
    time.sleep(.15)
    moveServo(bl2, heightDirections[height], heightAngles[height])
    moveServo(bl3, heightDirections[height], heightAngles[height])
    time.sleep(.125)
    if moveNow:
      moveServo(bl1, 1, 0)
      time.sleep(.15)
  elif legID == "br":
    moveServo(br2, dir, abs(temp2))
    moveServo(br3, dir, abs(temp2))
    time.sleep(.125)
    moveServo(br1, legDirection, amountMoved)
    time.sleep(.15)
    moveServo(br2, heightDirections[height], heightAngles[height])
    moveServo(br3, heightDirections[height], heightAngles[height])
    time.sleep(.125)
    if moveNow:
      moveServo(br1, 1, 0)
      time.sleep(.15)

def standup():
  moveServo(fl2, 1, 75)
  moveServo(fl3, 1, 75)
  moveServo(fr2, 1, 75)
  moveServo(fr3, 1, 75)
  moveServo(bl2, 1, 75)
  moveServo(bl3, 1, 75)
  moveServo(br2, 1, 75)
  moveServo(br3, 1, 75)
  time.sleep(.15)
  moveServo(fl2, -1, 30)
  moveServo(fr2, -1, 30)
  moveServo(bl2, -1, 30)
  moveServo(br2, -1, 30)  
  time.sleep(.15)
  moveServo(fl3, -1, 15)
  moveServo(fr3, -1, 15)
  moveServo(bl3, -1, 15)
  moveServo(br3, -1, 15)
  time.sleep(.15)
  moveServo(fl2, -1, 60)
  moveServo(fr2, -1, 60)
  moveServo(bl2, -1, 60)
  moveServo(br2, -1, 60)
  moveServo(fl3, -1, 60)
  moveServo(fr3, -1, 60)
  moveServo(bl3, -1, 60)
  moveServo(br3, -1, 60)
  time.sleep(.2)
  moveServo(fl2, -1, 90)
  moveServo(fr2, -1, 90)
  moveServo(bl2, -1, 90)
  moveServo(br2, -1, 90)
  time.sleep(.125)
  moveServo(fl2, -1, 90)
  moveServo(fr2, -1, 90)
  moveServo(bl2, -1, 90)
  moveServo(br2, -1, 90)

def moveBodyForward(h): 
  if h == 0:
    moveServo(fl2, 1, 45)
    moveServo(fl3, 1, 45)
    moveServo(br2, 1, 45)
    moveServo(br3, 1, 45)
    time.sleep(.125)
    moveServo(fl1, 1, 30)
    moveServo(br1, 1, 30)
    time.sleep(.125)
    moveServo(fl2, 1, 30)
    moveServo(fl3, 1, 30)
    moveServo(br2, 1, 30)
    moveServo(br3, 1, 30)
    time.sleep(.125)
    
    moveServo(fr2, 1, 45)
    moveServo(fr3, 1, 45)
    moveServo(bl2, 1, 45)
    moveServo(bl3, 1, 45)
    time.sleep(.125)
    moveServo(fr1, 1, 30)
    moveServo(bl1, 1, 30)
    time.sleep(.125)
    moveServo(fr2, 1, 30)
    moveServo(fr3, 1, 30)
    moveServo(bl2, 1, 30)
    moveServo(bl3, 1, 30)
    time.sleep(.125)

    moveServo(fl1, 1, 0)
    moveServo(br1, 1, 0)
    moveServo(bl1, 1, 0)
    moveServo(fr1, 1, 0)
    time.sleep(.125)

  elif h == 1:
    moveServo(fl2, 1, 30)
    moveServo(fl3, 1, 30)
    moveServo(br2, 1, 30)
    moveServo(br3, 1, 30)
    time.sleep(.125)
    moveServo(fl1, 1, 30)
    moveServo(br1, 1, 30)
    time.sleep(.125)
    moveServo(fl2, 1, 0)
    moveServo(fl3, 1, 0)
    moveServo(br2, 1, 0)
    moveServo(br3, 1, 0)
    time.sleep(.125)
    
    moveServo(fr2, 1, 30)
    moveServo(fr3, 1, 30)
    moveServo(bl2, 1, 30)
    moveServo(bl3, 1, 30)
    time.sleep(.125)
    moveServo(fr1, 1, 30)
    moveServo(bl1, 1, 30)
    time.sleep(.125)
    moveServo(fr2, 1, 0)
    moveServo(fr3, 1, 0)
    moveServo(bl2, 1, 0)
    moveServo(bl3, 1, 0)
    time.sleep(.125)

    moveServo(fl1, 1, 0)
    moveServo(br1, 1, 0)
    moveServo(bl1, 1, 0)
    moveServo(fr1, 1, 0)
    time.sleep(.125)

  elif h == 2:
    if mode == 0:
      moveServo(fl2, -1, 30)
      moveServo(fl3, -1, 30)
      moveServo(br2, -1, 30)
      moveServo(br3, -1, 30)
      time.sleep(.125)
      moveServo(fl1, 1, 45)
      moveServo(br1, 1, 45)
      time.sleep(.125)

      moveServo(fl3, -1, 45)    
      moveServo(br3, -1, 45)
      time.sleep(.15)
      moveServo(fl2, -1, 90)
      moveServo(br2, -1, 90)
      time.sleep(.1)
      moveServo(fl3, -1, 90)    
      moveServo(br3, -1, 90)

      moveServo(fr2, -1, 30)
      moveServo(fr3, -1, 30)
      moveServo(bl2, -1, 30)
      moveServo(bl3, -1, 30)
      time.sleep(.125)
      moveServo(fl1, 1, 0)
      moveServo(br1, 1, 0)
      time.sleep(.125)

      moveServo(fr1, 1, 45)
      moveServo(bl1, 1, 45)
      time.sleep(.125)

      moveServo(fr3, -1, 45)
      moveServo(bl3, -1, 45)
      time.sleep(.15)
      moveServo(fr2, -1, 90)
      moveServo(bl2, -1, 90)
      time.sleep(.1)
      moveServo(fr3, -1, 90)
      moveServo(bl3, -1, 90)
      time.sleep(.125)

      moveServo(bl1, 1, 0)
      moveServo(fr1, 1, 0)
      time.sleep(.125)
    elif mode == 1:
      moveLegStraight("fl", 1, 30, 45, False)
      moveLegStraight("br", 1, 30, 45, False)
      moveLegStraight("fr", 1, 30, 45, False)
      moveLegStraight("bl", 1, 30, 45, False)
      setHeight(height)

def moveBodyBack(h):
  if h == 0:
    moveServo(fl2, 1, 45)
    moveServo(fl3, 1, 45)
    moveServo(br2, 1, 45)
    moveServo(br3, 1, 45)
    time.sleep(.125)
    moveServo(fl1, -1, 30)
    moveServo(br1, -1, 30)
    time.sleep(.125)
    moveServo(fl2, 1, 30)
    moveServo(fl3, 1, 30)
    moveServo(br2, 1, 30)
    moveServo(br3, 1, 30)
    time.sleep(.125)
    
    moveServo(fr2, 1, 45)
    moveServo(fr3, 1, 45)
    moveServo(bl2, 1, 45)
    moveServo(bl3, 1, 45)
    time.sleep(.125)
    moveServo(fr1, -1, 30)
    moveServo(bl1, -1, 30)
    time.sleep(.125)
    moveServo(fr2, 1, 30)
    moveServo(fr3, 1, 30)
    moveServo(bl2, 1, 30)
    moveServo(bl3, 1, 30)
    time.sleep(.125)

    moveServo(fl1, 1, 0)
    moveServo(br1, 1, 0)
    moveServo(bl1, 1, 0)
    moveServo(fr1, 1, 0)
    time.sleep(.125)

  elif h == 1:
    moveServo(fl2, 1, 30)
    moveServo(fl3, 1, 30)
    moveServo(br2, 1, 30)
    moveServo(br3, 1, 30)
    time.sleep(.125)
    moveServo(fl1, -1, 30)
    moveServo(br1, -1, 30)
    time.sleep(.125)
    moveServo(fl2, 1, 0)
    moveServo(fl3, 1, 0)
    moveServo(br2, 1, 0)
    moveServo(br3, 1, 0)
    time.sleep(.125)
    
    moveServo(fr2, 1, 30)
    moveServo(fr3, 1, 30)
    moveServo(bl2, 1, 30)
    moveServo(bl3, 1, 30)
    time.sleep(.125)
    moveServo(fr1, -1, 30)
    moveServo(bl1, -1, 30)
    time.sleep(.125)
    moveServo(fr2, 1, 0)
    moveServo(fr3, 1, 0)
    moveServo(bl2, 1, 0)
    moveServo(bl3, 1, 0)
    time.sleep(.125)

    moveServo(fl1, 1, 0)
    moveServo(br1, 1, 0)
    moveServo(bl1, 1, 0)
    moveServo(fr1, 1, 0)
    time.sleep(.125)

  elif h == 2:
    moveServo(fl2, -1, 30)
    moveServo(fl3, -1, 30)
    moveServo(br2, -1, 30)
    moveServo(br3, -1, 30)
    time.sleep(.125)
    moveServo(fl1, -1, 30)
    moveServo(br1, -1, 30)
    time.sleep(.125)
    moveServo(fl2, -1, 90)
    moveServo(fl3, -1, 90)
    moveServo(br2, -1, 90)
    moveServo(br3, -1, 90)
    time.sleep(.125)
    
    moveServo(fr2, -1, 30)
    moveServo(fr3, -1, 30)
    moveServo(bl2, -1, 30)
    moveServo(bl3, -1, 30)
    time.sleep(.125)
    moveServo(fr1, -1, 30)
    moveServo(bl1, -1, 30)
    time.sleep(.125)
    moveServo(fr2, -1, 90)
    moveServo(fr3, -1, 90)
    moveServo(bl2, -1, 90)
    moveServo(bl3, -1, 90)
    time.sleep(.125)

    moveServo(fl1, 1, 0)
    moveServo(br1, 1, 0)
    moveServo(bl1, 1, 0)
    moveServo(fr1, 1, 0)
    time.sleep(.125)

def rotateBodyClockwise(h):
  if h == 0:
    moveServo(fr2, 1, 45)
    moveServo(fr3, 1, 45)
    moveServo(bl2, 1, 45)
    moveServo(bl3, 1, 45)
    time.sleep(.125)
    moveServo(fr1, -1, 30)
    moveServo(bl1, 1, 30)
    time.sleep(.15)
    moveServo(fr2, 1, 30)
    moveServo(fr3, 1, 30)
    moveServo(bl2, 1, 30)
    moveServo(bl3, 1, 30)
    time.sleep(.125)

    moveServo(fl2, 1, 45)
    moveServo(fl3, 1, 45)
    moveServo(br2, 1, 45)
    moveServo(br3, 1, 45)
    time.sleep(.125)
    moveServo(fl1, 1, 30)
    moveServo(br1, -1, 30)
    time.sleep(.15)
    moveServo(fl2, 1, 30)
    moveServo(fl3, 1, 30)
    moveServo(br2, 1, 30)
    moveServo(br3, 1, 30)
    time.sleep(.125)

    time.sleep(.125)
    moveServo(fr1, 1, 0)
    moveServo(br1, 1, 0)
    moveServo(bl1, 1, 0)
    moveServo(fl1, 1, 0)
    time.sleep(.125)
    
  elif h == 1:
    if mode == 0:
      moveServo(fr2, 1, 30)
      moveServo(fr3, 1, 30)
      moveServo(bl2, 1, 30)
      moveServo(bl3, 1, 30)
      time.sleep(.125)
      moveServo(fr1, -1, 30)
      moveServo(bl1, 1, 30)
      time.sleep(.15)
      moveServo(fr2, 1, 0)
      moveServo(fr3, 1, 0)
      moveServo(bl2, 1, 0)
      moveServo(bl3, 1, 0)
      time.sleep(.125)

      moveServo(fl2, 1, 30)
      moveServo(fl3, 1, 30)
      moveServo(br2, 1, 30)
      moveServo(br3, 1, 30)
      time.sleep(.125)
      moveServo(fl1, 1, 30)
      moveServo(br1, -1, 30)
      time.sleep(.15)
      moveServo(fl2, 1, 0)
      moveServo(fl3, 1, 0)
      moveServo(br2, 1, 0)
      moveServo(br3, 1, 0)
      time.sleep(.125)

      time.sleep(.125)
      moveServo(fr1, 1, 0)
      moveServo(br1, 1, 0)
      moveServo(bl1, 1, 0)
      moveServo(fl1, 1, 0)
      time.sleep(.125)
    elif mode == 1:
      moveServo(fr2, 1, 30)
      moveServo(fr3, 1, 30)
      time.sleep(.125)
      moveServo(fr1, -1, 30)
      time.sleep(.15)
      moveServo(fr2, 1, 0)
      moveServo(fr3, 1, 0)

      moveServo(bl2, 1, 30)
      moveServo(bl3, 1, 30)
      time.sleep(.125)
      moveServo(bl1, 1, 30)
      time.sleep(.15)
      moveServo(bl2, 1, 0)
      moveServo(bl3, 1, 0)

      moveServo(br2, 1, 30)
      moveServo(br3, 1, 30)
      time.sleep(.125)
      moveServo(br1, -1, 30)
      time.sleep(.15)
      moveServo(br2, 1, 0)
      moveServo(br3, 1, 0)

      moveServo(fl2, 1, 30)
      moveServo(fl3, 1, 30)
      time.sleep(.125)
      moveServo(fl1, 1, 30)
      time.sleep(.15)
      moveServo(fl2, 1, 0)
      moveServo(fl3, 1, 0)
      
      time.sleep(.125)
      moveServo(fr1, 1, 0)
      moveServo(br1, 1, 0)
      moveServo(bl1, 1, 0)
      moveServo(fl1, 1, 0)
      time.sleep(.125)

  elif h == 2:
    moveServo(fr2, -1, 60)
    moveServo(fr3, -1, 60)
    moveServo(bl2, -1, 60)
    moveServo(bl3, -1, 60)
    time.sleep(.125)
    moveServo(fr1, -1, 30)
    moveServo(bl1, 1, 30)
    time.sleep(.15)
    moveServo(fr2, -1, 90)
    moveServo(fr3, -1, 90)
    moveServo(bl2, -1, 90)
    moveServo(bl3, -1, 90)
    time.sleep(.125)

    moveServo(fl2, -1, 60)
    moveServo(fl3, -1, 60)
    moveServo(br2, -1, 60)
    moveServo(br3, -1, 60)
    time.sleep(.125)
    moveServo(fl1, 1, 30)
    moveServo(br1, -1, 30)
    time.sleep(.15)
    moveServo(fl2, -1, 90)
    moveServo(fl3, -1, 90)
    moveServo(br2, -1, 90)
    moveServo(br3, -1, 90)
    time.sleep(.125)

    time.sleep(.125)
    moveServo(fr1, 1, 0)
    moveServo(br1, 1, 0)
    moveServo(bl1, 1, 0)
    moveServo(fl1, 1, 0)
    time.sleep(.125)

def rotateBodyCounterClockwise(h):
  if h == 0:
    moveServo(fl2, 1, 45)
    moveServo(fl3, 1, 45)
    moveServo(br2, 1, 45)
    moveServo(br3, 1, 45)
    time.sleep(.125)
    moveServo(fl1, -1, 30)
    moveServo(br1, 1, 30)
    time.sleep(.15)
    moveServo(fl2, 1, 30)
    moveServo(fl3, 1, 30)
    moveServo(br2, 1, 30)
    moveServo(br3, 1, 30)
    time.sleep(.125)
    
    moveServo(fr2, 1, 45)
    moveServo(fr3, 1, 45)
    moveServo(bl2, 1, 45)
    moveServo(bl3, 1, 45)
    time.sleep(.125)
    moveServo(fr1, 1, 30)
    moveServo(bl1, -1, 30)
    time.sleep(.15)
    moveServo(fr2, 1, 30)
    moveServo(fr3, 1, 30)
    moveServo(bl2, 1, 30)
    moveServo(bl3, 1, 30)
    time.sleep(.125)

    time.sleep(.125)
    moveServo(fr1, 1, 0)
    moveServo(br1, 1, 0)
    moveServo(bl1, 1, 0)
    moveServo(fl1, 1, 0)
    time.sleep(.125)

  elif h == 1:
    if mode == 0:
      moveServo(fl2, 1, 30)
      moveServo(fl3, 1, 30)
      moveServo(br2, 1, 30)
      moveServo(br3, 1, 30)
      time.sleep(.125)
      moveServo(fl1, -1, 30)
      moveServo(br1, 1, 30)
      time.sleep(.15)
      moveServo(fl2, 1, 0)
      moveServo(fl3, 1, 0)
      moveServo(br2, 1, 0)
      moveServo(br3, 1, 0)
      time.sleep(.125)

      moveServo(fr2, 1, 30)
      moveServo(fr3, 1, 30)
      moveServo(bl2, 1, 30)
      moveServo(bl3, 1, 30)
      time.sleep(.125)
      moveServo(fr1, 1, 30)
      moveServo(bl1, -1, 30)
      time.sleep(.15)
      moveServo(fr2, 1, 0)
      moveServo(fr3, 1, 0)
      moveServo(bl2, 1, 0)
      moveServo(bl3, 1, 0)
      time.sleep(.125)

      time.sleep(.125)
      moveServo(fr1, 1, 0)
      moveServo(br1, 1, 0)
      moveServo(bl1, 1, 0)
      moveServo(fl1, 1, 0)
      time.sleep(.125)
    elif mode == 1:
      moveServo(fl2, 1, 30)
      moveServo(fl3, 1, 30)
      time.sleep(.125)
      moveServo(fl1, -1, 30)
      time.sleep(.15)
      moveServo(fl2, 1, 0)
      moveServo(fl3, 1, 0)

      moveServo(br2, 1, 30)
      moveServo(br3, 1, 30)
      time.sleep(.125)
      moveServo(br1, 1, 30)
      time.sleep(.15)
      moveServo(br2, 1, 0)
      moveServo(br3, 1, 0)

      moveServo(bl2, 1, 30)
      moveServo(bl3, 1, 30)
      time.sleep(.125)
      moveServo(bl1, -1, 30)
      time.sleep(.15)
      moveServo(bl2, 1, 0)
      moveServo(bl3, 1, 0)

      moveServo(fr2, 1, 30)
      moveServo(fr3, 1, 30)
      time.sleep(.125)
      moveServo(fr1, 1, 30)
      time.sleep(.15)
      moveServo(fr2, 1, 0)
      moveServo(fr3, 1, 0)
      
      time.sleep(.125)
      moveServo(fl1, 1, 0)
      moveServo(bl1, 1, 0)
      moveServo(br1, 1, 0)
      moveServo(fr1, 1, 0)
      time.sleep(.125)

  elif h == 2:
    moveServo(fl2, -1, 60)
    moveServo(fl3, -1, 60)
    moveServo(br2, -1, 60)
    moveServo(br3, -1, 60)
    time.sleep(.125)
    moveServo(fl1, -1, 30)
    moveServo(br1, 1, 30)
    time.sleep(.15)
    moveServo(fl2, -1, 90)
    moveServo(fl3, -1, 90)
    moveServo(br2, -1, 90)
    moveServo(br3, -1, 90)
    time.sleep(.125)

    moveServo(fr2, -1, 60)
    moveServo(fr3, -1, 60)
    moveServo(bl2, -1, 60)
    moveServo(bl3, -1, 60)
    time.sleep(.125)
    moveServo(fr1, 1, 30)
    moveServo(bl1, -1, 30)
    time.sleep(.15)
    moveServo(fr2, -1, 90)
    moveServo(fr3, -1, 90)
    moveServo(bl2, -1, 90)
    moveServo(bl3, -1, 90)
    time.sleep(.125)

    time.sleep(.125)
    moveServo(fr1, 1, 0)
    moveServo(br1, 1, 0)
    moveServo(bl1, 1, 0)
    moveServo(fl1, 1, 0)
    time.sleep(.125)

while not joy.connected():
  time.sleep(1)

setUpArrays()
tweekValues()
bootup()

while joy.connected():
  # This shuts down the turtle
  if joy.Back():
    break
  elif joy.Start():
    standup()

  elif joy.leftY() == 1:
    moveBodyForward(height)
  elif joy.leftY() == -1:
    moveBodyBack(height)
  elif joy.rightX() == 1:
    rotateBodyClockwise(height)
  elif joy.rightX() == -1:
    rotateBodyCounterClockwise(height)
  
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
    moveServo(fl1, 1, 30)
    moveServo(bl1, 1, 30)
    moveServo(fr1, -1, 30)
    moveServo(br1, -1, 30)
    time.sleep(.125)
    moveServo(fl1, -1, 30)
    moveServo(bl1, -1, 30)
    moveServo(fr1, 1, 30)
    moveServo(br1, 1, 30)
    time.sleep(.15)
    setHeight(height)
    time.sleep(.125)
  elif joy.A():
    for x in range(0, mode+1):
      moveServo(br2, 1, 15)
      moveServo(br3, 1, 15)
      time.sleep(.15)
      setHeight(height)
      time.sleep(.15)
  elif joy.B():
    if mode == 0:
      moveServo(fl1, 1, 30)
      moveServo(fl2, -1, 30)
      moveServo(fl3, -1, 30)
      moveServo(fr1, 1, 30)
      moveServo(fr2, -1, 30)
      moveServo(fr3, -1, 30)
      moveServo(bl1, -1, 30)
      moveServo(bl2, -1, 30)
      moveServo(bl3, -1, 30)
      moveServo(br1, -1, 30)
      moveServo(br2, -1, 30)
      moveServo(br3, -1, 30)
      time.sleep(.5)
      setHeight(height)
      time.sleep(.25)
    elif mode == 1:
      moveServo(fl1, -1, 30)
      moveServo(fl2, -1, 30)
      moveServo(fl3, -1, 30)
      moveServo(fr1, -1, 30)
      moveServo(fr2, -1, 30)
      moveServo(fr3, -1, 30)
      moveServo(bl1, 1, 30)
      moveServo(bl2, -1, 30)
      moveServo(bl3, -1, 30)
      moveServo(br1, 1, 30)
      moveServo(br2, -1, 30)
      moveServo(br3, -1, 30)
      time.sleep(.5)
      setHeight(height)
      time.sleep(.25)
    elif mode == 2:
      moveServo(fl1, -1, 30)
      moveServo(fl2, -1, 30)
      moveServo(fl3, -1, 30)
      moveServo(fr1, -1, 30)
      moveServo(fr2, -1, 30)
      moveServo(fr3, -1, 30)
      moveServo(bl1, -1, 30)
      moveServo(bl2, -1, 30)
      moveServo(bl3, -1, 30)
      moveServo(br1, -1, 30)
      moveServo(br2, -1, 30)
      moveServo(br3, -1, 30)
      time.sleep(.5)
      setHeight(height)
      time.sleep(.25)
    elif mode == 3:
      moveServo(fl1, 1, 30)
      moveServo(fl2, -1, 30)
      moveServo(fl3, -1, 30)
      moveServo(fr1, 1, 30)
      moveServo(fr2, -1, 30)
      moveServo(fr3, -1, 30)
      moveServo(bl1, 1, 30)
      moveServo(bl2, -1, 30)
      moveServo(bl3, -1, 30)
      moveServo(br1, 1, 30)
      moveServo(br2, -1, 30)
      moveServo(br3, -1, 30)
      time.sleep(.5)
      setHeight(height)
      time.sleep(.25)
  elif joy.Y():
    if mode == 0:
      moveServo(fl1, 1, 30)
      moveServo(fr1, 1, 30)
      moveServo(bl1, 1, 30)
      moveServo(br1, 1, 30)
      time.sleep(.5)
      moveServo(fl1, -1, 30)
      moveServo(fr1, -1, 30)
      moveServo(bl1, -1, 30)
      moveServo(br1, -1, 30)
      time.sleep(.125)
      setHeight(height)
      time.sleep(.125)
    elif mode == 1:
      moveServo(fl2, 1, 30)
      moveServo(fl3, 1, 30)
      moveServo(fr2, 1, 30)
      moveServo(fr3, 1, 30)
      moveServo(bl2, -1, 30)
      moveServo(bl3, -1, 30)
      moveServo(br2, -1, 30)
      moveServo(br3, -1, 30)
      time.sleep(.125)
      setHeight(height)
      time.sleep(.125)
    elif mode == 2:
      moveServo(fl2, -1, 30)
      moveServo(fl3, -1, 30)
      moveServo(fr2, -1, 30)
      moveServo(fr3, -1, 30)
      moveServo(bl2, 1, 30)
      moveServo(bl3, 1, 30)
      moveServo(br2, 1, 30)
      moveServo(br3, 1, 30)
      time.sleep(.125)
      setHeight(height)
      time.sleep(.125)
    elif mode == 3:
      moveServo(fr2, 1, 30)
      moveServo(fr3, -1, 90)
      moveServo(fr1, 1, 75)
      bashCommand = "omxplayer -o local butch.mp3"
      process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
      #output, error = process.communicate()
      time.sleep(.125)
      setHeight(height)
      time.sleep(.15)

  findLeftRegion()
joy.close()

shutdown()