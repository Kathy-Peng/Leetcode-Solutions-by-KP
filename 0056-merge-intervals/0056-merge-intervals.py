class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #step 1: sort the intervals from small to large
        intervals = sorted(intervals)
        #step 2: initialize the ret list which contains the first item to begin with
        ret = [intervals[0]]
        #step 3: loop from the second item to end of list
        for i in range(1,len(intervals)):
            curr = intervals[i]
            #if there is overlapping between the current item and the last item in ret
            if curr[0]<=ret[-1][1]:
                #update the ret list to be the larger of the end time
                ret[-1][1]=max(curr[1], ret[-1][1])
            else:
                #if not overlapping, add the current item to ret list
                ret.append(curr)  
        return ret
        
            
            