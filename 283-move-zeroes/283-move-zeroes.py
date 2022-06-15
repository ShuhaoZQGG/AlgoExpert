class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastZeroIndex = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastZeroIndex] = nums[i]
                lastZeroIndex += 1
        
        for i in range(lastZeroIndex, len(nums), 1):
            nums[i] = 0