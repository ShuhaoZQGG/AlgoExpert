class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = collections.Counter()
        maxF = 0
        res = 0 
        l, r = 0, 0
        while l < len(s):
            counter[s[r]] += 1
            maxF = max(maxF, counter[s[r]])
            if r - l - maxF + 1 <= k:
                res += 1
            else:
                counter[s[l]] -= 1
                l += 1
            if r == len(s) - 1 and r - l <= res:
                return res
            r += 1
        return res