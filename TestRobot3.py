from Robot import *
from Path import *
from Calibrate import *
from AngleConverter import *
from PathHandler import *
from Navigator import *

# load a path file
p = Path("Path-around-table.json")
path = p.getPath()

print("Path length = " + str(len(path)))
print("First point = " + str(path[0]['X']) + ", " + str(path[0]['Y']))

# make a robot to move around
robot = Robot()
converter = AngleConverter()
pathHandler = PathHandler()
navigator = Navigator()

#### Intialize variables
position = {}
speed = 0.4
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
    print(nextPoint)

    ### find direction to path
    directionToPoint = navigator.getDirection( position, path, nextPoint )    
    turnRate = navigator.getTurnRate( heading, directionToPoint )

    ### set motion
    robot.setMotion(speed, turnRate )
    time.sleep(0.5)
    robot.setMotion(0,0 )

