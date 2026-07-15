class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        ans = 0
        while (low <= high):
            mid = int((low + high)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                ans = mid + 1
                low = mid +1
            else:
                high = mid -1
        return ans                
        