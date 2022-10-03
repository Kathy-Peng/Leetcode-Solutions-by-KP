class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        #loop through every node of the grid
        #if this node is already visited or it's a 0 ignore
        #otherwise explore it using BFS helper function
        visited = set()
        row = len(grid)
        col = len(grid[0])
        count = 0
        
        def bfs(grid, i, j):
            queue = [(i,j)]
            while len(queue)!=0:
                curr = queue.pop(0)
                i,j = curr[0],curr[1]
                iorw = grid[i][j]
                #conditions for adding to the visited list
                #1. not out of bounds 2. not visited 3. same type: island or water
                if i>0:
                    if (i-1,j) not in visited and grid[i-1][j]==iorw: #up
                        queue.append((i-1,j))
                        visited.add((i-1,j))
                if j>0:
                    if (i,j-1) not in visited and grid[i][j-1]==iorw: #left
                        queue.append((i,j-1))
                        visited.add((i,j-1))
                if i<row-1:
                    if (i+1,j) not in visited and grid[i+1][j]==iorw: #down
                        queue.append((i+1,j))
                        visited.add((i+1,j))
                if j<col-1:
                    if (i,j+1) not in visited and grid[i][j+1]==iorw:#right
                        queue.append((i,j+1))
                        visited.add((i,j+1))
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and (i,j) not in visited:
                    bfs(grid, i, j)
                    count += 1
        return count
        
            