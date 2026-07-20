class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_mp = {}
        for i in range(len(nums)):
            hash_mp[nums[i]] = i
        for j in range(len(nums)):
            x = target - nums[j]
            if x in hash_mp:
                if hash_mp[x] != j:
                    return [j,hash_mp[x]]
        return -1                
