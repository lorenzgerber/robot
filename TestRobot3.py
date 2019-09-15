from Robot import Robot
from time import sleep
from Path import Path
from Calibrate import Calibrate
from AngleConverter import AngleConverter
from PathHandler import PathHandler
from Navigator import Navigator
from Goal import Goal

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
goal = Goal()

#### Intialize variables
position = robot.getPosition()
speed = 0.3
heading = 0
nextPoint = 0
dropOut = 0
lookAheadDistance = 1

while ( goal.notGoal( position, nextPoint, path ) ):

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
    sleep(0.5)
    robot.setMotion(0,0 )


print('Geeeeeehaaaaaaa')

