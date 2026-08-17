class Solution:
    def  subset_Combination(self,index,subset,ans,nums,target):
        if target == 0:
            ans.append(subset.copy())
            return
        elif index >= len(nums) or target < 0:
            return
        subset.append(nums[index])
        self.subset_Combination(index + 1,subset,ans,nums,target-nums[index])
        subset.pop()
        x = nums[index]
        while index < len(nums) and nums[index] == x:
            index +=1
        self.subset_Combination(index,subset,ans,nums,target) 

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        index = 0
        ans = []
        candidates.sort()
        subset = []
        self.subset_Combination(index,subset,ans,candidates,target)
        return ans