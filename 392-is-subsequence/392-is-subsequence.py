class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        ptrS = 0
        for ptrT in range(len(t)):
            if s[ptrS] == t[ptrT]:
                ptrS += 1
            if ptrS == len(s):
                return True
        if ptrS < len(s):
            return False
        else:
            return True