class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        frq_val = 0
        for num in nums:
            if num == val:
                frq_val +=1
        l = 0
        h = len(nums)-frq_val
        while(h < len(nums) and l < len(nums)):
            if nums[l] != val:
                l+=1
            elif nums[l] == val and nums[h] != val:
                nums[l],nums[h] = nums[h],nums[l]
                h+=1
                l+=1
            elif nums[h] == val:
                h+=1
        return len(nums) - frq_val
        