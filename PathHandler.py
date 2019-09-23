from math import pow, sqrt

class PathHandler:


    def getNextPathPoint ( self, position, path, startPoint, lookaheadDistance, lookaheadSwitchDistance ):

        ### set variable
        currentPoint = startPoint
        currentDistance = 0

        distanceToStartPoint = self.calculateDistance(position['X'], position['Y'], path[startPoint]['X'], path[startPoint]['Y'])


        if ( distanceToStartPoint < lookaheadSwitchDistance ):
            while ( currentDistance < lookaheadDistance ):
                currentDistance = self.calculateDistance(position['X'], position['Y'], path[currentPoint]['X'], path[currentPoint]['Y'])
                currentPoint = currentPoint + 1
                if(self.isLastPoint(path, currentPoint)):
                    currentDistance = 999999

            currentPoint = currentPoint - 1
       
        return ( currentPoint )
    
    def isLastPoint ( self, path, currentPoint):
        if ( currentPoint == (len(path) - 1)):
            return True
        
        return ( False )


    def calculateDistance ( self, xHome, yHome, xAway, yAway ):
            distance = sqrt(pow(xAway - xHome, 2) + pow(yAway - yHome, 2))
            return ( distance )

