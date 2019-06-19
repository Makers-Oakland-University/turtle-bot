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
            currArray.append(625)
        else:
            currArray.append(0)

one =   [150, 188]
two =   [225, 263]
three = [300, 338]
four =  [375, 413]
five =  [450, 488]
six =   [525, 563]
servo = [one, two, three, four, five, six]

testArray = []
fillDefaultArray(testArray)
print(testArray)
testArray = testArray[::-1]
print(testArray)

print(servo[1][0])
print("Complete")