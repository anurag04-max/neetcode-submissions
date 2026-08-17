class Solution:
    def subsetSum(self, index, nums, current_xor):
        if index == len(nums):
            return current_xor

        # Include nums[index]
        include = self.subsetSum(
            index + 1,
            nums,
            current_xor ^ nums[index]
        )

        # Don't include nums[index]
        exclude = self.subsetSum(
            index + 1,
            nums,
            current_xor
        )

        return include + exclude

    def subsetXORSum(self, nums: List[int]) -> int:
        return self.subsetSum(0, nums, 0)