from math import degrees, pi, radians, sin, pow

class Calculator:

    def convertToDegree( self, angle ):
        if(angle < 0):
            return ( degrees( -angle ))
        else:
            return ( degrees( pi - angle + pi))

    def getTurnRate( self, intercept, maxTurn ):
        turnRate = -(maxTurn * sin(radians(180+(intercept/2))))
        return turnRate




