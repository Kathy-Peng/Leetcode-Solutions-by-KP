class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        to_ret = [[0 for i in range(row)] for j in range(col)]
        for i in range(col):
            for j in range(row):
                to_ret[i][j] = matrix[j][i]
        return to_ret