class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        setB = set(bobSizes)
        diff = (sumB - sumA)/2
        for x in aliceSizes:
            if x + diff in setB:
                return [x, x + diff]
        
        

        