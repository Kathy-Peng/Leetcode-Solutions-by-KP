import heapq

class Pair:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, p):
        return self.freq < p.freq or (self.freq == p.freq and self.word > p.word)

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        heapify(heap)
        frequency = Counter(words)
        for word, freq in frequency.items():
            heappush(heap, Pair(word, freq))
            if len(heap) > k:
                heappop(heap)
        return [item.word for item in sorted(heap, reverse=True)]




            
            
            
            
        