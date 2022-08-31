class Solution(object):
    def calc_area(self,height, i,j):
            return min(height[i], height[j])*(j-i)
        
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height)-1
        
        maxArea = 0
        while i<j:
            area = self.calc_area(height,i,j)
            maxArea = max(maxArea, area)
            
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
                
        return maxArea
        
            
            