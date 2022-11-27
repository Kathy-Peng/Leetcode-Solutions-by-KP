class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        xp = 0
        yp = n
        new_list = []
        while yp < 2*n:
            new_list.append(nums[xp])
            new_list.append(nums[yp])
            xp += 1
            yp += 1
        return new_list
            