class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot = 0
        prefix = 0
        while pivot < len(nums):
            if prefix == sum(nums[pivot + 1 : len(nums)]):
                return pivot
            prefix += nums[pivot]
            pivot += 1
        return -1