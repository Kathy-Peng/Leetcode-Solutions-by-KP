class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        dist = 0
        while xor:
            if xor % 2:
                dist += 1
            xor = xor >> 1
        return dist