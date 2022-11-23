from heapq import heapify, heappop, heappush
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []
        heapify(heap)
        count = 0
        for item in intervals:
            if len(heap)==0:
                heappush(heap,item[1])
                count += 1
            else:
                if item[0] < heap[0]:
                    count += 1   
                else: # contains larger and equal to 
                    heappop(heap)
                heappush(heap, item[1])
        return count