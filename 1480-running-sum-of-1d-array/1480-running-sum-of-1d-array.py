class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prev = 0
        for i in range(len(nums)):
            iThNum = nums[i]
            nums[i] += prev
            prev += iThNum
        return nums