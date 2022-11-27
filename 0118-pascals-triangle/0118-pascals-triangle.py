class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for i in range(numRows-1):
            output = [1]
            prev = result[-1]
            for j in range(len(prev)-1):
                output.append(prev[j]+prev[j+1])
            output.append(1)
            result.append(output)
        return result
            