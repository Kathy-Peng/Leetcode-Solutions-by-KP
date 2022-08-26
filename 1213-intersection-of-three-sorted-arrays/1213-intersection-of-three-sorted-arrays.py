class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        hashmap = {}
        res= []
        arr = arr1 + arr2 + arr3
        for item in arr:
            if item not in hashmap:
                hashmap[item]=1
            else:
                curr = hashmap[item]
                hashmap[item]=curr+1
                if hashmap[item]==3:
                    res.append(item)
        return res