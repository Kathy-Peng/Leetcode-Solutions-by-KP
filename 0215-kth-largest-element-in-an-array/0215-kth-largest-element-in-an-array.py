from heapq import heapify, heappush, heappop, nsmallest
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapify(heap)
        for item in nums:
            if len(heap)==0:
                heappush(heap, item)
            elif len(heap) < k:
                heappush(heap, item)
            else:
                if item > heap[0]:
                    heappop(heap)
                    heappush(heap, item)
        return heap[0]
                
        