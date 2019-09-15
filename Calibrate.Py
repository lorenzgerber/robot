from Robot import Robot
from time import sleep
from math import atan2, sqrt, pow
from AngleConverter import AngleConverter

class Calibrate:

    def __init__(self, Robot):

        self.robot = Robot    
    
    def calibrate(self):
        self.acquireData()
        self.calculateAngle()

    def acquireData(self):
        self.heading = self.robot.getHeading()
        self.startPosition = self.robot.getPosition()
        self.robot.setMotion(0.1, 0)
        sleep(5)
        self.robot.setMotion(0,0)
        self.stopPosition = self.robot.getPosition()

    def calculateAngle(self):
        print(self.startPosition)
        dx = self.stopPosition.get('X') - self.startPosition.get('X')
        dy = self.stopPosition.get('Y') - self.startPosition.get('Y')
        angle = atan2(dy, dx)
        distance = sqrt( pow(dx,2) + pow(dy,2) )
        converter = AngleConverter()
        print(angle)
        print(converter.convertToDegree(angle))
        print(distance)


   
