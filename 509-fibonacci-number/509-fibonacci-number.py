class Solution:
    def fib(self, n: int) -> int:
        dp = [0, 1]
        counter = 2
        if n == 0:
            return dp[n]
        
        if n == 1:
            return dp[n]
        
        for i in range(n):
            dp[i % 2] = dp[0] + dp[1]
            
        if n % 2 == 0:
            return dp[0]
        else:
            return dp[1]
        
        