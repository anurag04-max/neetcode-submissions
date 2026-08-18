class Solution:
    def duplicates(self,index,nums,subset,ans):
        if index == len(nums):
            ans.append(subset.copy())
            return
        subset.append(nums[index])
        self.duplicates(index + 1,nums,subset,ans)
        subset.pop()
        x = nums[index]
        while index < len(nums) and x == nums[index]:
            index +=1
        self.duplicates(index,nums,subset,ans)
            

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        index = 0
        subset = []
        ans = []
        self.duplicates(index,nums,subset,ans)
        return ans