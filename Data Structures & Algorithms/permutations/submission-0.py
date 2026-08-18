class Solution:
    def permutations(self,nums,freq,subset,ans):
        if len(subset) == len(nums):
            ans.append(subset.copy())
            return
        for i in range(len(nums)):
            if freq.get(i,0) == 0:
                freq[i] = 1
                subset.append(nums[i])
                self.permutations(nums,freq,subset,ans)
                freq[i] = 0
                subset.pop()        


    def permute(self, nums: List[int]) -> List[List[int]]:
        freq = {}
        subset = []
        ans = []
        index = 0
        self.permutations(nums,freq,subset,ans)
        return ans