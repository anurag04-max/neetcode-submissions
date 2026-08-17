class Solution:
    def subset_Sum(self,index,subset,nums:List[int],target:int,ans):
        if target == 0:
            ans.append(subset.copy())
            return
        elif index  >= len(nums) or target < 0:
            return
        subset.append(nums[index])
        self.subset_Sum(index,subset,nums,target-nums[index],ans)
        subset.pop()
        self.subset_Sum(index + 1,subset,nums,target,ans)       

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        index = 0
        ans = []
        subset = []
        self.subset_Sum(index,subset,nums,target,ans)
        return ans