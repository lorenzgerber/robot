from math import atan2
from AngleConverter import * 

class Navigator:
    


    def getDirection ( self, position, path, pathIndex ):

        converter = AngleConverter()

        dx = path[pathIndex]['X'] - position['X']
        dy = path[pathIndex]['Y'] - position['Y']
        angle = atan2(dy, dx)
        angle = converter.convertToDegree(angle)

        return ( angle )

    def getTurnRate (self, heading, directionToPoint ):

        turnRate = 0.3

        metric = (heading - directionToPoint) % 360
        if ( metric >= 180.0 ):
            turnRate = turnRate * -1
        
        return ( turnRate )