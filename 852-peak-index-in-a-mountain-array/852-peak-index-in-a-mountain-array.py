class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        #we find the peak if it's larger than both the left and the right
        l= 1
        r=len(arr)-2
        while l <= r:
            mid = (l+r)/2
            print(mid)
            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid
            if arr[mid]<arr[mid-1]:
                r = mid - 1
            if arr[mid]<arr[mid+1]:
                l = mid + 1
        