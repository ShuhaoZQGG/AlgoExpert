class Solution:
    def isHappy(self, n: int) -> bool:
        hs = set()
        while n != 1:
            n = sum(int(c) ** 2 for c in str(n))
            if n in hs:
                return False
            hs.add(n)
        return True