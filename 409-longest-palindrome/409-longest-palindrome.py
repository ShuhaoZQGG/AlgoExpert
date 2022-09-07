class Solution:
    def longestPalindrome(self, s: str) -> int:
        hm = {}
        ans = 0
        highOdd = 0
        for c in s:
            if c in hm:
                hm[c] += 1
            else:
                hm[c] = 1
                
        for k, v in hm.items():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                    ans += 1
        ans += highOdd
        return ans

