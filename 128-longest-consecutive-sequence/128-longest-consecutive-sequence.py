class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        res = 1
        maxRes = 1
        for i, val in enumerate(nums):
            if val - nums[i - 1] != 0:
                if val - nums[i - 1] != 1:
                    maxRes = max(maxRes, res)
                    res = 1
                else:
                    res += 1
        maxRes = max(res, maxRes)
        return maxRes
            