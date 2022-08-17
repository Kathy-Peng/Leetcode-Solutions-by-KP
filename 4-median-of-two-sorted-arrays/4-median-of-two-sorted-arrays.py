class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """ 
        i = 0
        j = 0
        merge_list = []
        while i < len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                merge_list.append(nums1[i])
                i+=1
            else:
                merge_list.append(nums2[j])
                j+=1
        while i<len(nums1):
            merge_list.append(nums1[i])
            i+=1
        while j<len(nums2):
            merge_list.append(nums2[j])
            j+=1
        if len(merge_list)%2==0:
            return float((merge_list[len(merge_list)//2]+merge_list[len(merge_list)//2-1]))/2
        else:
            return merge_list[len(merge_list)//2]
            
            
            
            
        