class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        start = m
        low = 0
        while(start < m + n):
            nums1[start] = nums2[low]
            low +=1
            start+=1
        nums1.sort()    
