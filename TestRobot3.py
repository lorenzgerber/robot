from Robot import *
from Path import *
from Calibrate import *
from AngleConverter import *
from PathHandler import *

# load a path file
p = Path("Path-around-table.json")
path = p.getPath()

print("Path length = " + str(len(path)))
print("First point = " + str(path[0]['X']) + ", " + str(path[0]['Y']))

# make a robot to move around
robot = Robot()
converter = AngleConverter()
pathHandler = PathHandler()
# calibration = Calibrate(robot)
# calibration.calibrate()
# print(converter.convertToDegree(robot.getHeading()))
# robot.setMotion(0,0.104)
# sleep(60)
# robot.setMotion(0,0)
# print(converter.convertToDegree(robot.getHeading()))
# dropOut = False

#### Intialize variables
position = {}
speed = 0.5
heading = 0
nextPoint = 0
dropOut = 0
lookAheadDistance = 1

while ( dropOut < 100 ):

    ### get current status (position, heading)
    position = robot.getPosition()
    heading = converter.convertToDegree(robot.getHeading())
    
    ### get next point
    nextPoint = pathHandler.getNextPathPoint( position, path, nextPoint, lookAheadDistance)

    ### {X, Y} getNextPath (pathList, startEntry, lookaheadDistance)
        ### current position
        ### loop through path entries
            ### calculate distance

    ### find direction to path
        ### angle to next point
        ### which direction to turn
        ### determine actual angle 

    ### set motion

