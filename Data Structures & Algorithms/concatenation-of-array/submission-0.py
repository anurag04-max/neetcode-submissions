class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        ans = []
        while (i <= 2*n - 1):
            ans.append(nums[(i% n)])
            i += 1
        return ans