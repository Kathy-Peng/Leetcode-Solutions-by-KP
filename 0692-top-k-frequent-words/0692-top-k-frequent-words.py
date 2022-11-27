# import heapq
# class Solution:
#     def topKFrequent(self, words: List[str], k: int) -> List[str]:
#         heap = []
#         heapify(heap)
#         frequency = Counter(words)
#         for word, freq in frequency.items():
#             if len(heap) < k:
#                 heappush(heap, (freq, word))
#             else:
#                 if freq > heap[0][0] or freq == heap[0][0] and word < heap[0][1]:
#                     heappop(heap)
#                     heappush(heap, (freq, word))
#         return [item[1] for item in sorted(heap, reverse=True)]
        
from collections import Counter
from heapq import heappush, heappop


class Pair:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, p):
        return self.freq < p.freq or (self.freq == p.freq and self.word > p.word)


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        h = []
        for word, freq in cnt.items():
            heappush(h, Pair(word, freq))
            if len(h) > k:
                heappop(h)
        return [p.word for p in sorted(h, reverse=True)]
                    
            
            
            
            
            
            
        