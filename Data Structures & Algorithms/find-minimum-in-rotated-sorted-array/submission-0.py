class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) -1
        ans = nums[0]
        while(l <= h):
            mid = (l + h) // 2
            if nums[mid] <= nums[h]:
                ans = min(ans, nums[mid])
                h = mid -1
            else:
                l = mid + 1   
        return ans       

        