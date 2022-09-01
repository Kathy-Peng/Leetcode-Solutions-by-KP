class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        i = 0
        j = len(height)-1
        maxleft = height[i]
        maxright = height[j]
        water_stored = 0
        while i < j:
            if maxleft < maxright:
                i+=1
                maxleft = max(maxleft, height[i])
                water_stored += maxleft - height[i]
            else:
                j-=1
                maxright = max(maxright, height[j])
                water_stored += maxright - height[j]
        return water_stored
                 
            
        
            
            
        
                
            
            
                
        
        
        