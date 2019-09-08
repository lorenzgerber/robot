from Robot import *
from Path import *
from Calibrate import *
from AngleConverter import *

# load a path file
p = Path("Path-around-table.json")
path = p.getPath()

print("Path length = " + str(len(path)))
print("First point = " + str(path[0]['X']) + ", " + str(path[0]['Y']))

# make a robot to move around
robot = Robot()
converter = AngleConverter()
calibration = Calibrate(robot)
calibration.calibrate()
print(converter.convertToDegree(robot.getHeading()))
robot.setMotion(0,0.104)
sleep(60)
robot.setMotion(0,0)
print(converter.convertToDegree(robot.getHeading()))

