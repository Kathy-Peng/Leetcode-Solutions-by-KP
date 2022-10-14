class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        ret = [intervals[0]]
        print(intervals)
        for i in range(1,len(intervals)):
            curr = intervals[i]
            prev = intervals[i-1]
            if curr[0]<=ret[-1][1]:
                ret[-1][1]=max(curr[1], ret[-1][1])
            else:
                ret.append(curr)  
        return ret
        
            
            