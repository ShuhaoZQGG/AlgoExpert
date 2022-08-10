class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        Sum = sum(nums)
        pivot = 0
        prefix = 0
        while pivot < len(nums):
            if prefix == Sum - prefix - nums[pivot]:
                return pivot
            prefix += nums[pivot]
            pivot += 1
        return -1