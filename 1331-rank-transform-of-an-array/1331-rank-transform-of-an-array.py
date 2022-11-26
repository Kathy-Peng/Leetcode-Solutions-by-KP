class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_copy = arr[:]
        arr_copy.sort()
        hashmap = {}
        rank = 1
        for item in arr_copy:
            if item not in hashmap:
                hashmap[item] = rank
                rank += 1
        result = []
        for item in arr:
            result.append(hashmap[item])        
        return result
            