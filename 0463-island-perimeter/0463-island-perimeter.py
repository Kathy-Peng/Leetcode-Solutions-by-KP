class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        height = len(grid)
        width = len(grid[0])
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                   
                    perimeter += 4
                    if i-1 >= 0 and grid[i-1][j]:
                        perimeter -= 1
          
                    if i+1 < height and grid[i+1][j]:
                        perimeter -= 1
                 
                    if j+1 < width and grid[i][j+1]:
                        perimeter -= 1
                      
                    if j-1 >= 0 and grid[i][j-1]:
                       
                        perimeter -= 1
                
        return perimeter
                    
                