class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        initial = prices[0]
        for price in prices[1:]:
          initial = min(initial, price)
          maxProfit = max(maxProfit, price - initial)
        return maxProfit