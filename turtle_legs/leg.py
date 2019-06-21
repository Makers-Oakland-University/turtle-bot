import time

import config

shoulderPos = 1
elbowPos = 2
wristPos = 3

class Leg:
    def __init__(self, shoulderServoNumber, elbowServoNumber, wristServoNumber, leftSideOfBody):
        self.shoulderAngles = []
        self.elbowAngles = []
        self.wristAngles = []
        self.fillDefaultArray(self.shoulderAngles)
        self.fillDefaultArray(self.elbowAngles)
        self.fillDefaultArray(self.wristAngles)
        if leftSideOfBody:
            self.shoulderAngles = self.shoulderAngles[::-1]
            self.elbowAngles = self.elbowAngles[::-1]
            self.wristAngles = self.wristAngles[::-1]
        #elif rightSideOfBody == True:
            #self.elbowAngles = self.elbowAngles[::-1]
            #self.wristAngles = self.wristAngles[::-1]

        self.shoulderServoNumber = shoulderServoNumber
        self.elbowServoNumber = elbowServoNumber
        self.wristServoNumber = wristServoNumber

        self.shoulderAngle = 0
        self.elbowAngle = 0
        self.wristAngle = 0
        self.leftSideOfBody = leftSideOfBody

    def move(self, shoulderAngle, elbowAngle, wristAngle, sleepTime):
        if (shoulderAngle != "current"):
            if config.moveServo(self.shoulderServoNumber, self.shoulderAngles[90 + shoulderAngle]):
                self.shoulderAngle = shoulderAngle
        if (elbowAngle != "current"):
            if config.moveServo(self.elbowServoNumber, self.elbowAngles[90 + elbowAngle]):
                self.elbowAngle = elbowAngle
        if (wristAngle != "current"):
            if config.moveServo(self.wristServoNumber, self.wristAngles[90 + wristAngle]):
                self.wristAngle = wristAngle
        time.sleep(sleepTime)

    def fillDefaultArray(self, currArray):
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

    def tweekValue(self, jointNumber, angle, newValue):
        if jointNumber == shoulderPos:
            self.shoulderAngles[angle] = newValue
        elif jointNumber == elbowPos:
            self.elbowAngles[angle] = newValue
        elif jointNumber == wristPos:
            self.wristAngles[angle] = newValue
