from Robot import Robot
from time import sleep
from Path import Path
from PathHandler import PathHandler
from Navigator import Navigator

# Settings
maxSpeed = 0.5
lookAheadDistance = 0.7
maxTurnRate = 1.2
damperLength = 7

#### Intialize 
robot = Robot()
p = Path("Path-around-table-and-back.json")
path = p.getPath()
pathHandler = PathHandler()
navigator = Navigator( maxSpeed, maxTurnRate, damperLength )
robot.setMotion(0, 0)
position = robot.getPosition()
heading = 0
nextPoint = 0

while ( navigator.notGoal( position, nextPoint, path ) ):

    ### get current status (position, heading)
    position = robot.getPosition()
    heading = navigator.convertToDegree(robot.getHeading())
    
    ### get next point
    nextPoint = pathHandler.getNextPathPoint( position, path, nextPoint, lookAheadDistance)

    ### find direction to path
    directionToPoint = navigator.getDirection( position, path, nextPoint )    
    
    ### get turn direction +/- maximum turn rate
    turnDirection = navigator.getTurnDirection( heading, directionToPoint )
    
    ### determine dynamic turn rate based on interecpt angle
    turnRate = navigator.getTurnRate( directionToPoint, turnDirection )
    
    ### apply a dampler on the turn rate output
    turnRate = navigator.dampen( turnRate)

    ### dynamic speed adjustment according turnRate (currently not in use)
    #speed = navigator.adjustSpeed( turnRate )
    speed = maxSpeed

    ### set motion
    robot.setMotion(speed, turnRate )
    sleep(0.05)

robot.setMotion( 0,0 )
sleep(1)