class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
      left, right = 1, max(piles)
      while left < right:
        mid = (left + right) // 2
        k = 0
        for i in range(len(piles)):
          k += math.ceil(piles[i] / mid)
        
        if k <= h:
          right = mid
        else:
          left = mid + 1
          
      return right