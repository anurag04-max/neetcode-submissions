class Solution:
    def subset_calculator(self,index,nums,cur_subset,ans):
        if index >= len(nums):
            ans.append(cur_subset.copy())
            return
        cur_subset.append(nums[index])    
        self.subset_calculator(index + 1,nums,cur_subset,ans)
        cur_subset.pop()      
        self.subset_calculator(index + 1,nums,cur_subset,ans)
       
  
    def subsets(self, nums: List[int]) -> List[List[int]]:
        cur_subset = []
        ans = []
        index = 0
        self.subset_calculator(index,nums,cur_subset,ans)
        return ans