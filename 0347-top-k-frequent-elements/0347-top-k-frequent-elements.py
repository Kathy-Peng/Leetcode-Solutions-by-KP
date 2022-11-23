class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for item in nums:
            if item not in hashmap:
                hashmap[item]=1
            else:
                hashmap[item]+=1
        new_list = [(hashmap[item], item) for item in hashmap]
        new_list.sort(reverse=True)
        result = [item[1] for item in new_list[:k]]
        return result