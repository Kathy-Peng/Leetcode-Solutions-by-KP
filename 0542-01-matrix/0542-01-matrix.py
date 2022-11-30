class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        result = [[0 for i in range(n)] for j in range(m)]
        visited = [[0 for i in range(n)] for j in range(m)]
        queue = []
        #add all 0s to the queue
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    visited[i][j]=1
                    queue.append(((i,j)))
                    
        dist = 0 
        while len(queue):
            for i in range(len(queue)):
                row, col = queue.pop(0)
                if mat[row][col]==1:
                    result[row][col]=dist
                if row+1 < m and not visited[row+1][col]:
                    #if the down neighbor is valid and not visited
                    queue.append((row+1, col))
                    visited[row+1][col]=1
                if col+1 < n and not visited[row][col+1]:
                    queue.append((row, col+1))
                    visited[row][col+1]=1
                if row-1 >= 0 and not visited[row-1][col]:
                    queue.append((row-1, col))
                    visited[row-1][col] =1
                if col-1 >= 0 and not visited[row][col-1]:
                    queue.append((row, col-1))
                    visited[row][col-1] = 1
            dist += 1
        return result
                
        