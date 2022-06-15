class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        target = 0
        for i in range(len(digits)):
            target += digits[i] * (10 ** (len(digits) - i - 1))
        target += 1
        while target > 0:
            res.append(target % 10)
            target //= 10
        res.reverse()
        return res