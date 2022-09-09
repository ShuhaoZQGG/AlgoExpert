class Solution:
    def fib(self, n: int) -> int:
        dp = [0, 1]
        counter = 2
        if n == 0:
            return dp[n]
        
        if n == 1:
            return dp[n]
        
        while n >= 2:
            if counter % 2 == 0:
                dp[0] = dp[0] + dp[1]
            else:
                dp[1] = dp[0] + dp[1]
            n -= 1
            counter += 1
            
        if counter%2 == 0:
            return dp[1]
        else:
            return dp[0]
        
        