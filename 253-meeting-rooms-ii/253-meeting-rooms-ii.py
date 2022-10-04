
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        start = []
        end = []
        for item in intervals:
            start.append(item[0])
            end.append(item[1])
        start.sort()
        end.sort()
        l1, l2 = 0,0
        max_count, count = 0,0 
        while l1<len(intervals) and l2<len(intervals):
            if start[l1]<end[l2]:
                count += 1
                if count > max_count:
                    max_count = count
                l1 += 1
            else: 
                #if one meeting starts at the same time another meeting ends
                #we don't count them as overlapping and decrement the meeting
                count -= 1
                l2 += 1
        return max_count
                
            
            
                