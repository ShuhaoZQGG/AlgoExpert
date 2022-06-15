class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastZeroIndex = 0
        # Move all non-zeros to the front, and then increment index
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastZeroIndex] = nums[i]
                lastZeroIndex += 1
        
        # the number of zeros = length - index
        # fill the number of zeros at the end
        for i in range(lastZeroIndex, len(nums), 1):
            nums[i] = 0