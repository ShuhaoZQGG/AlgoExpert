class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def isTwoZeros(nums):
          count = 0
          for i in range(len(nums)):
            if nums[i] == 0:
              count += 1
          if count >= 2:
            return True
          return False
        
        product = 1
        non_zero_product = 1
        if isTwoZeros(nums):
          return [0]*len(nums)
        for i in range(len(nums)):
          if nums[i] != 0:
            non_zero_product *= nums[i]
          product *= nums[i]
        for i in range(len(nums)):
          if nums[i] == 0:
            nums[i] = non_zero_product
          else:
            nums[i] = product // nums[i]

        return nums