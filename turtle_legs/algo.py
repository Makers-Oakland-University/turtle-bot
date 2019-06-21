from json import JSONEncoder
import json
from time import sleep

# algoSet = []
# algoSet.append({
#     'Name': 'Point',
#     'Positions': [['fl', 11, 12, 5, 0], ['fl', 15, 6, 10, 0], ['fl', 10, 8, 12, 0], ['fl', 12, 15, 8, 0]]
# })
# with open('algos.json', 'w') as outfile:  
#     json.dump(algoSet, outfile)
# sleep(1)

data = None
with open('algos.json') as json_file:  
    data = json.load(json_file)

for p in data:
    print 'Move Name: ' + p['move_name']
    for i in range(len(p['servo_positions'])):
        print 'Position' , i+1
        print "Leg:", p['servo_positions'][i][0]
        print "Shoulder Position:", p['servo_positions'][i][1]
        print "Elbow Position:", p['servo_positions'][i][2]
        print "Wrist Position:", p['servo_positions'][i][3]
        print "Sleep Duration:", p['servo_positions'][i][4]
        print ''
    print ''
    print ''

# class MobilePhone:
#     contacts = None
#     apps     = None

#     def __init__(self, contacts, apps):
#         self.contacts   = contacts
#         self.apps       = apps

#     def startCall():
#         pass

#     def endCall():
#         pass

# class MobilePhoneEncoder(JSONEncoder):
#     def default(self, object):
#         if isinstance(object, MobilePhone):
#             return object.__dict__
#         else:
#             # call base class implementation which takes care of
#             # raising exceptions for unsupported types
#             return json.JSONEncoder.default(self, object)


# algoName = "Test Movement"
# randPositions = [[11, 12, 5], [15, 6, 10], [10, 8, 12], [12, 15 ,8]]
# algo = [algoName, randPositions]

# algoSet = []
# algoSet.append(algo)

# class AlgoSet:
#     def __init__(self, move):
#         self.algo = []
#         self.algoAngles = []
#         self.algoNames.append("Test Movement")
#         self.algoAngles

# class Algo:
#     def __init__(self):
#         self.name = "Test Movement"
#         self.positions = [[11, 12, 5], [15, 6, 10], [10, 8, 12], [12, 15 ,8]]


# class AlgoSetEncoder(JSONEncoder):
#     def default(self, object):
#         if isinstance(object, AlgoSet):
#             return object.__dict__
#         else:
#             # call base class implementation which takes care of
#             # raising exceptions for unsupported types
#             return json.JSONEncoder.default(self, object)

# class AlgoEncoder(JSONEncoder):
#     def default(self, object):
#         if isinstance(object, Algo):
#             return object.__dict__
#         else:
#             # call base class implementation which takes care of
#             # raising exceptions for unsupported types
#             return json.JSONEncoder.default(self, object)

# testAlgo = Algo()
# testAlgoSet = AlgoSet(testAlgo)
# 4
# jsonString = AlgoSetEncoder().encode(testAlgoSet)
# print jsonString