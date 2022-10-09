class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        together_list = list(set1)+list(set2)
        hashmap = {}
        for item in together_list:
            if item in hashmap:
                hashmap[item] += 1
            else:
                hashmap[item]=1
        results = []
        for item in hashmap:
            if hashmap[item]>1:
                results.append(item)
        return results
        
        
            
        