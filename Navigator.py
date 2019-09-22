from math import atan2, sin, radians, degrees, pi, sqrt

class Navigator:

    def __init__(self, maxSpeed, maxTurnRate, damperLength ):
        self.damper = [0]
        self.maxSpeed = maxSpeed
        self.maxTurnRate = maxTurnRate
        self.damperLength = damperLength
    
    def convertToDegree( self, angle ):
        if(angle < 0):
            return ( degrees( -angle ))
        else:
            return ( degrees( pi - angle + pi))
    
    def getDirection ( self, position, path, pathIndex ):

        dx = path[pathIndex]['X'] - position['X']
        dy = path[pathIndex]['Y'] - position['Y']
        angle = atan2(dy, dx)
        angle = self.convertToDegree(angle)

        return ( angle )

    def getTurnDirection (self, heading, directionToPoint ):

        turnRate = self.maxTurnRate

        metric = (heading - directionToPoint) % 360
        if ( metric >= 180.0 ):
            turnRate = turnRate * -1
        
        return ( turnRate )

    def getTurnRate( self, intercept, maxTurn ):
        turnRate = -(maxTurn * sin(radians(180+(intercept/2))))
        return turnRate

    def dampen( self, turnRate ):
        self.damper.append(turnRate)
        self.damper = self.damper[-self.damperLength:]

        if(sum(self.damper)!= 0):
            turnRate = sum(self.damper) / len(self.damper)
        
        return ( turnRate )

    def notGoal( self, position, nextPoint, path ):

        currentDistance = self.calculateDistance(position['X'], position['Y'], path[-1]['X'], path[-1]['Y'])
        if (currentDistance > 1 ):
                return( True )
        else:
            if( nextPoint != (len(path)-2)):
                return( True )
        return( False )

    def calculateDistance ( self, xHome, yHome, xAway, yAway ):
        distance = sqrt(pow(xAway - xHome, 2) + pow(yAway - yHome, 2))
        return ( distance )

    def adjustSpeed( self, turnRate ):
        percentOfMaxTurnRate = 1/self.maxTurnRate * abs(turnRate)
        speed = (1 - percentOfMaxTurnRate) * self.maxSpeed  + (0.2 * self.maxSpeed)
        if (speed > self.maxSpeed):
            speed = self.maxSpeed
        return (speed)

