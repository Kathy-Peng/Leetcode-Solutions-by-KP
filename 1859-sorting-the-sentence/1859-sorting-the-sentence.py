import heapq
class Solution:
    def sortSentence(self, s: str) -> str:
        heap = []
        heapify(heap)
        s = s.split(' ')
        for word in s:
            idx = word[-1]
            heappush(heap, (idx, word[:-1]))
        result = []
        while len(heap):
            result.append(heappop(heap)[1])
        return ' '.join(result)
            
        