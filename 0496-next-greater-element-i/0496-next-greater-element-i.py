class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        stk = []
        for i in range(len(nums2)-1, -1, -1):
            val = nums2[i]
            if len(stk)==0:
                #stk is initially empty, return -1
                hashmap[val]=-1
                stk.append(val)
                continue
            if val < stk[-1]:
                #if top of stk is larger than val, return top of stk
                hashmap[val]=stk[-1]
                stk.append(val)
            else:
                #val is larger than top of stk, pop until smaller
                while len(stk)!=0 and val > stk[-1]:
                    stk.pop()
                if len(stk)==0:
                    #cannot find value if stk larger than val, return -1
                    hashmap[val]= -1
                else:
                    #return the closest larger value than val
                    hashmap[val] = stk[-1]
                stk.append(val)
                    
        #construct the answer array using hashmap
        ans = []
        for item in nums1:
            ans.append(hashmap[item])
        return ans
                
    