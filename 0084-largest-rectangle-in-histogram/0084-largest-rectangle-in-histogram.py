class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] #tuple of (idx, height)
        for idx, height in enumerate(heights):
            if not len(stack):
                stack.append((idx, height))
            if stack[-1][1] <= height:
                stack.append((idx, height))
            else:
                while stack and stack[-1][1] > height:
                    prev_idx, prev_height = stack.pop()
                    max_area = max(max_area, (idx-prev_idx)*prev_height)
                stack.append((prev_idx, height))
                    
        for idx, height in stack:
            max_area = max(max_area, (len(heights) - idx) * height)
        return max_area
                
            
                
                