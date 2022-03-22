class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        array = [1, 2]
        
        for i in range(n - 2):
            array.append(array[-1] + array[-2])
        
        return array[-1]