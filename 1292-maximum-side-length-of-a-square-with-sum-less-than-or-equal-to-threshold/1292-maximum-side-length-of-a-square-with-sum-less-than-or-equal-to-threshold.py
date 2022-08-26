
class Solution(object):
          
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        def exists(mid):
            for i in range(row-mid+1):
                for j in range(col-mid+1):
                    if pre_sum[i][j]-pre_sum[i][j+mid]-pre_sum[i+mid][j]+pre_sum[i+mid][j+mid]<= threshold:
                        return True
            return False
    
        row = len(mat)
        col = len(mat[0])
        #pad 1 for both row and col to avoid going out of boundaries
        pre_sum = [ [0]*(col+1) for _ in range(row+1)]
        for i in range(row-1, -1, -1):
            for j in range(col-1,-1,-1):
                pre_sum[i][j]=mat[i][j]+pre_sum[i+1][j] + pre_sum[i][j+1]-pre_sum[i+1][j+1]
        
        l = 0
        r = min(len(mat),len(mat[0]))
        
        while l < r:
            mid = l + ( r - l + 1) / 2
            if exists(mid):
                l = mid
            else:
                r = mid - 1
        return l
                