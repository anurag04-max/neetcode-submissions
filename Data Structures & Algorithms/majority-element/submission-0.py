class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_mp = {}
        n = len(nums)
        for num in nums:
            hash_mp[num] = hash_mp.get(num,0) + 1
        for x,v in hash_mp.items():
            if v >= n // 2:
                return x
        return -1            
        