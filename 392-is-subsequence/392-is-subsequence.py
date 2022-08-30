class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        
        ptrT = 0
        for i in range(len(t)):
            if t[i] == s[ptrT]:
                ptrT += 1
            
            if len(s) == ptrT:
                return True
            
        if ptrT < len(s):
            return False
        else:
            return True
            