class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        #step 1: intialize a hash map which maps parent to its child node
        hashmap = {}
        for i in range(len(pid)):
            if ppid[i] not in hashmap:
                hashmap[ppid[i]]=[pid[i]]
            else:
                curr = hashmap[ppid[i]]
                curr.append(pid[i])
                hashmap[ppid[i]]=curr
        
        to_kill = [kill]
        stack = [kill]
        while len(stack)!=0:
            curr = stack.pop()
            if curr not in hashmap:
                continue
            for child in hashmap[curr]:
                to_kill.append(child)
                stack.append(child)
        return to_kill
            
            
        