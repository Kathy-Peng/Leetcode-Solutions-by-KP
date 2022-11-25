class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] #tuple of (idx, height)
        for idx, height in enumerate(heights):
            start = idx
            #if there is a dip, calculate max_area with all the heights larger than the dipped height
            while stack and stack[-1][1] > height:
                prev_idx, prev_height = stack.pop()
                max_area = max(max_area, (idx-prev_idx)*prev_height)
                start = prev_idx
            stack.append((start, height))
                    
        for idx, height in stack:
            max_area = max(max_area, (len(heights) - idx) * height)
        return max_area
                
            
                
                