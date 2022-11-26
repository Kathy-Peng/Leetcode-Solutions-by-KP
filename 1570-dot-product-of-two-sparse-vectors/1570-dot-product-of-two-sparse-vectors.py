class SparseVector:
    def __init__(self, nums: List[int]):
        self.hashmap = {}
        self.dim = len(nums)
        for i in range(len(nums)):
            if nums[i]!=0:
                self.hashmap[i]=nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        hashmap2 = vec.hashmap
        final = []
        for i in range(self.dim):
            if i in self.hashmap and i in hashmap2:
                final.append(self.hashmap[i] * hashmap2[i])
        return sum(final)
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)