from math import pow, sqrt

class Goal:

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
    