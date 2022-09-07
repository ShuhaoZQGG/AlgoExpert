class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highestP = 0
        buy = prices[0]
        for i in range(len(prices)):
            buy = min(buy, prices[i])
            profit = prices[i] - buy
            highestP = max(profit, highestP)
        return highestP