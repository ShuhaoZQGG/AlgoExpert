class Solution:
    def isHappy(self, n: int) -> bool:
        while n != 1:
            if n < 10 and n != 1 and n != 7:
                return False
            n = sum(int(c) ** 2 for c in str(n))

        return True