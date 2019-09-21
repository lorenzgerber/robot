from Robot import Robot
from time import sleep
from Path import Path
from Calibrate import Calibrate
from Calculator import Calculator
from AngleConverter import AngleConverter
from PathHandler import PathHandler
from Navigator import Navigator
from Goal import Goal

# load a path file
p = Path("Path-around-table-and-back.json")
path = p.getPath()

print("Path length = " + str(len(path)))
print("First point = " + str(path[0]['X']) + ", " + str(path[0]['Y']))

# make a robot to move around
robot = Robot()
converter = AngleConverter()
pathHandler = PathHandler()
navigator = Navigator()
calculator = Calculator()
goal = Goal()

#### Intialize variables
robot.setMotion(0, 0)
position = robot.getPosition()
speed = 0.4
heading = 0
nextPoint = 0
dropOut = 0
lookAheadDistance = 0.6
damper = [0]

while ( goal.notGoal( position, nextPoint, path ) ):

    ### get current status (position, heading)
    position = robot.getPosition()
    heading = converter.convertToDegree(robot.getHeading())
    
    ### get next point
    nextPoint = pathHandler.getNextPathPoint( position, path, nextPoint, lookAheadDistance)

    ### find direction to path
    directionToPoint = navigator.getDirection( position, path, nextPoint )    
    turnDirection = navigator.getTurnDirection( heading, directionToPoint )
    turnRate = calculator.getTurnRate( directionToPoint, turnDirection )
    damper.append(turnRate)
    damper = damper[-10:]

    if(sum(damper)!= 0):
        turnRate = sum(damper) / len(damper)


    ### set motion
    robot.setMotion(speed, turnRate )
    sleep(0.1)

robot.setMotion( 0,0 )