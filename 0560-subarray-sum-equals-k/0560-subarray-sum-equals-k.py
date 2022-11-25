class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = collections.defaultdict(int)
        hashmap[0] = 1
        result = 0
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            diff = prefix_sum - k
            if diff in hashmap:
                result += hashmap[diff]
            hashmap[prefix_sum] += 1
        return result