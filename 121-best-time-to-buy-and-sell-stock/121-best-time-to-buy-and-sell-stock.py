class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        lowest = prices[0]
        for i in range(len(prices)):
            lowest = min(lowest, prices[i])
            maxP = max(prices[i]-lowest, maxP)
        return maxP