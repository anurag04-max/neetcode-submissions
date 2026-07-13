class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a1 = m-1
        a2 = n-1
        mer = m + n - 1
        while mer >= 0:
            if a1 >= 0 and a2 >= 0 and nums1[a1] >= nums2[a2]:
                nums1[mer] = nums1[a1]
                a1 -=1
            elif a1 >= 0 and a2 >= 0 and nums1[a1] < nums2[a2]:
                nums1[mer] = nums2[a2]
                a2 -=1
            elif a1 >= 0:
                nums1[mer] = nums1[a1]
                a1-=1
            else:
                nums1[mer] = nums2[a2]
                a2 -=1
            mer -=1    





 
