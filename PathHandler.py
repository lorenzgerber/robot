from math import pow
from math import sqrt

class PathHandler:


    def getNextPathPoint ( self, position, path, startPoint, lookaheadDistance ):
       
       ### set variable
        currentPoint = startPoint
        currentDistance = 0
       
        while ( currentDistance < lookaheadDistance ):
            currentDistance = self.calculateDistance(position['X'], position['Y'], path[currentPoint]['X'], path[currentPoint]['Y'])
            currentPoint = currentPoint + 1
            if(self.isLastPoint(path, currentPoint)):
                currentDistance = 999999

        return ( currentPoint - 1 )
    
    def isLastPoint ( self, path, currentPoint):
        if ( currentPoint == (len(path) - 1)):
            return True
        
        return ( False )





    def calculateDistance ( self, xHome, yHome, xAway, yAway ):
            distance = sqrt(pow(xAway - xHome, 2) + pow(yAway - yHome, 2))
            return ( distance )

