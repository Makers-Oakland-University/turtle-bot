from time import sleep
from algo import Algo

tempMoveList = []
foundAlgo = False

class AlgoSet:
    def __init__(self, frontLeftLeg, frontRightLeg, backLeftLeg, backRightLeg):
        self.algoSet = []
        self.frontLeftLeg = frontLeftLeg
        self.frontRightLeg = frontRightLeg
        self.backLeftLeg = backLeftLeg
        self.backRightLeg = backRightLeg

    def addAlgo(self, algoName, algoPositions):
        self.algoSet.append(Algo(algoName, algoPositions))

    def run(self, algoToRun):
        for a in self.algoSet:
            if a.getName() == algoToRun:
                tempMoveList = a.getPositions()
                foundAlgo = True
        if foundAlgo:
            for move in tempMoveList:
                if move[0] == 'fl':
                    self.frontLeftLeg.move(move[1], move[2], move[3])
                elif move[0] == 'fr':
                    self.frontRightLeg.move(move[1], move[2], move[3])
                elif move[0] == 'bl':
                    self.backLeftLeg.move(move[1], move[2], move[3])
                elif move[0] == 'br':
                    self.backRightLeg.move(move[1], move[2], move[3])
                elif move[0] == 'sleep':
                    sleep(move[1]/1000)
            foundAlgo = False