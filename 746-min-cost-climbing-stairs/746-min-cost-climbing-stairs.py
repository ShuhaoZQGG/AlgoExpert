class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def minimum_cost(i):
            if i <= 1:
                return 0
            
            one_step = cost[i - 1] + minimum_cost(i - 1)
            two_steps = cost[i - 2] + minimum_cost(i - 2)
            return min(one_step, two_steps)
        return minimum_cost(len(cost))