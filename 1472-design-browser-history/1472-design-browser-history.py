class ListNode:
    def __init__(self, Prev, Next, val):
        self.prev = Prev
        self.next = Next
        self.val = val

class BrowserHistory:
    def __init__(self, homepage: str):
        self.homepage = ListNode(None, None, homepage)
        
    def visit(self, url: str) -> None:
        #step 1: add a node after the current homepage
        newNode = ListNode(self.homepage, None, url)
        self.homepage.next = newNode
        #step 2: update the self.homepage to be the current visiting website
        self.homepage = newNode
        
    def back(self, steps: int) -> str:
        x = 0
        curr = self.homepage
        while x < steps:
            if not curr.prev:
                self.homepage = curr
                return curr.val
            curr = curr.prev
            x += 1
        self.homepage = curr
        return curr.val
    
    def forward(self, steps: int) -> str:
        x = 0
        curr = self.homepage
        while x<steps:
            if not curr.next:
                self.homepage = curr
                return curr.val
            curr = curr.next
            x += 1
        self.homepage = curr
        return curr.val
    
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)