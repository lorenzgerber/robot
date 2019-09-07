from Robot import *
from Path import *

# load a path file
p = Path("Path-around-table.json")
path = p.getPath()

print("Path length = " + str(len(path)))
print("First point = " + str(path[0]['X']) + ", " + str(path[0]['Y']))

# make a robot to move around
robot = Robot()

# move the robot
robot.setMotion(0.2, 0.2)

for i in range(10):
    time.sleep(1)
    print("pos, heading");
    print(robot.getPosition())
    print(robot.getHeading())

echoes = robot.getLaser()
print(echoes)

robot.setMotion(0, 0)