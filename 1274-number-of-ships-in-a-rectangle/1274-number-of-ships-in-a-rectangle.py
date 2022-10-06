# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight, bottomLeft):
#        """
#        :type topRight: Point
#		 :type bottomLeft: Point
#        :rtype bool
#        """
#
#class Point(object):
#	def __init__(self, x, y):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea, topRight, bottomLeft):
        """
        :type sea: Sea
        :type topRight: Point
        :type bottomLeft: Point
        :rtype: integer
        """
        #define the base case which is when the input rectangle is a point
        if topRight.x < bottomLeft.x or topRight.y < bottomLeft.y:
            return 0
        if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            return 1 if sea.hasShips(topRight,bottomLeft) else 0
            
        #if this quadrant does not have ships at all return 0
        if not sea.hasShips(topRight, bottomLeft):
            return 0
        
        mid_x = (topRight.x + bottomLeft.x)// 2
        mid_y = (topRight.y + bottomLeft.y)// 2
        
        num_ships = 0
        p1 = Point(mid_x, mid_y) 
        #bottom left quadrant
        num_ships += self.countShips(sea, p1, bottomLeft)
        p2 = Point(bottomLeft.x, mid_y+1)
        p3 = Point(mid_x, topRight.y)
        #top left quadrant
        num_ships += self.countShips(sea,p3, p2)
        p4 = Point(mid_x+1 , mid_y +1)
        #top right quadrant
        num_ships += self.countShips(sea,topRight, p4)
        p5 = Point(mid_x+1, bottomLeft.y)
        p6 = Point(topRight.x, mid_y)
        #bottom right quadrant
        num_ships += self.countShips(sea,p6,p5)
        return num_ships
        
        
        
        