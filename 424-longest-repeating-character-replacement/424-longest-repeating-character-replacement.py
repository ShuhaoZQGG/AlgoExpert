class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = collections.Counter()
        maxF = 0
        res = 0 
        for i in range(len(s)):
            counter[s[i]] += 1
            maxF = max(maxF, counter[s[i]])
            if res - maxF < k:
                res += 1
            else:
                counter[s[i - res]] -=1
        return res