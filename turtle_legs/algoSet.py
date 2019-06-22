from algo import Algo
from config import frontLeftLeg, frontRightLeg, backLeftLeg, backRightLeg

tempMoveList = []
foundAlgo = False

class AlgoSet:
    def __init__(self):
        self.algoSet = []

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
                    frontLeftLeg.move(move[1], move[2], move[3], move[4])
                elif move[0] == 'fr':
                    frontRightLeg.move(move[1], move[2], move[3], move[4])
                elif move[0] == 'bl':
                    backLeftLeg.move(move[1], move[2], move[3], move[4])
                elif move[0] == 'br':
                    backRightLeg.move(move[1], move[2], move[3], move[4])
            foundAlgo = False