class Solution:
    def argsort(self, l):
        return sorted(range(len(l)),key=l.__getitem__)
    
    def frequencySort(self, s: str) -> str:
        hashmap = {}
        for char in s:
            if char in hashmap:
                hashmap[char]+=1
            else:
                hashmap[char]=1
        l = []
        c = []
        for char,freq in hashmap.items():
            l.append(freq)
            c.append(char)
        idx = self.argsort(l)
        des_idx = idx[::-1]
        ret = ''
        for i, idx in enumerate(des_idx):
            char = c[idx]
            freq = hashmap[char]
            ret = ret + char*freq
        return ret
        
        
            