import heapq
class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        heapify(self.max_heap)
        heapify(self.min_heap)
        self.len = 0

    def addNum(self, num: int) -> None:
        if self.len==0:
            heappush(self.max_heap, -num)
            self.len += 1
            return
        
        if num > -self.max_heap[0]:
            heappush(self.min_heap, num)
        else:
            heappush(self.max_heap, -num)
            
        if len(self.max_heap)-len(self.min_heap)>1:
            val = heappop(self.max_heap)
            heappush(self.min_heap, -val)
            
        elif len(self.min_heap)-len(self.max_heap)>1:
            val = heappop(self.min_heap)
            heappush(self.max_heap, -val)
            
        self.len += 1

    def findMedian(self) -> float:
        if self.len % 2:
            if len(self.max_heap)>len(self.min_heap):
                return -self.max_heap[0]
            else:
                return self.min_heap[0]
        else:
            val1 = self.min_heap[0] if len(self.min_heap) else 0
            val2 = -self.max_heap[0] if len(self.max_heap) else 0
            return (val1 + val2)/2
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()