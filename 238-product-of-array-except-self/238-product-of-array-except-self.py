class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # function to check if there are two or more than two zeros
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
        
        # return a list of 0 if there are two or more zeros in the nums
        if isTwoZeros(nums):
          return [0]*len(nums)
        
        # calculate the product of every num in nums
        for i in range(len(nums)):
          if nums[i] != 0:
            non_zero_product *= nums[i]
          product *= nums[i]
        
        # distinguish product and non_zero_product to prevent zero division exception
        for i in range(len(nums)):
          if nums[i] == 0:
            nums[i] = non_zero_product
          else:
            nums[i] = product // nums[i]

        return nums