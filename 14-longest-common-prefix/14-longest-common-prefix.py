class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestPrefix = strs[0]
        for string in strs:
            longestPrefix = self.getPrefix(longestPrefix, string)
        return longestPrefix
            
    def getPrefix(self, strA: str, strB: str):
        prefix = ""
        if len(strA) >= len(strB):
            strA, strB = strB, strA
        else:
            strA, strB = strA, strB
        for i in range(len(strA)):
            if strA[i] == strB[i]:
                prefix += strA[i]
            else:
                return prefix
        return prefix