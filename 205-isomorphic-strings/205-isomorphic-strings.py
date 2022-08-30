class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}
        
        for i in range(len(s)):
            map_s[s[i]] = t[i]
            map_t[t[i]] = s[i]
            
        for i in range(len(s)):
            if map_s[s[i]] != t[i] or map_t[t[i]] != s[i]:
                return False
        
        
        return True