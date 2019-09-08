from math import degrees
from math import pi

class AngleConverter:

    def convertToDegree( self, angle ):
        if(angle < 0):
            return ( degrees( -angle ))
        else:
            return ( degrees( pi - angle + pi))



