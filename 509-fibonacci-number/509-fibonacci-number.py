class Solution:
    def fib(self, n: int) -> int:
        res = [0, 1]
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        counter = n
        while counter >= 2:
            res.append(res[-1] + res[-2])
            counter -= 1
        return res[-1]
        