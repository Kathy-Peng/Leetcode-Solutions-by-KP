class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [(-f, c) for c, f in count.items()]
        heapq.heapify(maxHeap)
        res = ''
        prev = None
       
        while prev or maxHeap:
            if prev and not maxHeap:
                return ''
            f, c = heapq.heappop(maxHeap)
            res += c
            f += 1
            
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if f:
                prev = (f, c)
        return res
        