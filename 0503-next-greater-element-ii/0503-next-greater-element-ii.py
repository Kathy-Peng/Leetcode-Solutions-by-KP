class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stk = nums[:]
        stk.reverse()
        for i in range(len(nums)-1, -1, -1):
            val = nums[i]
            if val < stk[-1]:
                nums[i]=stk[-1]
                stk.append(val)
            else:
                while len(stk)!=0 and val >= stk[-1]:
                    stk.pop()
                if len(stk)==0:
                    nums[i]=-1
                else:
                    nums[i]=stk[-1]
                stk.append(val)
        return nums
                    
                    
                