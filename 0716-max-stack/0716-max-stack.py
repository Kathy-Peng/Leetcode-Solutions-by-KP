import heapq
class MaxStack:

    def __init__(self):
        self.stack = []
        self.max_heap = []
        heapify(self.max_heap)
        self.removed = set()
        self.count = 0

    def push(self, x: int) -> None:
        self.stack.append((x, self.count))
        heappush(self.max_heap, (-x,-self.count))
        self.count += 1

    def pop(self) -> int:
        while self.stack[-1][1] in self.removed:
            self.stack.pop()
        val, idx = self.stack.pop()
        self.removed.add(idx)
        return val
        
    def top(self) -> int:
        while self.stack[-1][1] in self.removed:
            self.stack.pop()
        return self.stack[-1][0]
    
    def peekMax(self) -> int:
        while -self.max_heap[0][1] in self.removed:
            heappop(self.max_heap)
        return -self.max_heap[0][0]
    
    def popMax(self) -> int:
        while -self.max_heap[0][1] in self.removed:
            heappop(self.max_heap)
        val, idx = heappop(self.max_heap)
        self.removed.add(-idx)
        return -val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()