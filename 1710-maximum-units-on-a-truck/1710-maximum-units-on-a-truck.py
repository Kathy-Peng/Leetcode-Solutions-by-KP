class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        for i in range(len(boxTypes)):
            reverse = boxTypes[i]
            reverse.reverse()
            boxTypes[i]=reverse
        boxTypes.sort(reverse =True)
        maxUnit = 0
        for j in range(len(boxTypes)):
            if truckSize == 0:
                break
            if boxTypes[j][1] < truckSize:
                maxUnit += boxTypes[j][1] * boxTypes[j][0]
                truckSize -= boxTypes[j][1]
            else:
                maxUnit += boxTypes[j][0] * truckSize
                truckSize = 0
        return maxUnit
                    