class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        
        self.inserted = {}
        self.returned = {}
    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        flag = True
        to_ret = []
        self.inserted[idKey]=value
        self.returned[idKey]=False
        #step 1: determine whether we need to return anything at all
        for i in range(1, idKey):
            if i not in self.inserted:
                flag = False
        #step 2: if we need to return anything, return only items that have not been returned yet, up until the last consecutive item
        if flag:
            idx = 1
            while idx in self.returned:
                if self.returned[idx]==False:
                    to_ret.append(self.inserted[idx])
                    self.returned[idx]=True
                idx = idx + 1
        return to_ret
        

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)