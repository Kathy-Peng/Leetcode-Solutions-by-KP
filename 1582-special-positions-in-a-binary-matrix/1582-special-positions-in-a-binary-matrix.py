class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row = len(mat)
        col = len(mat[0])
        count = 0
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 1:
                    row_list = mat[i]
                    col_list = [mat[r][j] for r in range(row)]
                    if sum(row_list) == 1 and sum(col_list)==1:
                        count += 1
        return count
                
            