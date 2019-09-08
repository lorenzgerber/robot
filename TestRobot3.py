from Robot import *
from Path import *
from Calibrate import *

# load a path file
p = Path("Path-around-table.json")
path = p.getPath()

print("Path length = " + str(len(path)))
print("First point = " + str(path[0]['X']) + ", " + str(path[0]['Y']))

# make a robot to move around
robot = Robot()
calibration = Calibrate(robot)
calibration.calibrate()
print(robot.getHeading())
robot.setMotion(0,0.104)
sleep(60)
robot.setMotion(0,0)
print(robot.getHeading())

