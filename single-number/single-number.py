class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        for i in range(len(nums)):
            if i + 1 < len(nums) and i - 1 >= 0:
                if (nums[i] != nums[i - 1] and nums[i] != nums[i + 1]):
                    return nums[i]
            elif i - 1 < 0:
                if nums[i] != nums[i + 1]:
                    return nums[i]
            else:
                if nums[i] != nums[i-1]:
                    return nums[i]