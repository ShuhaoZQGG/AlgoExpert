class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            if tuple(count) in ans:
                ans[tuple(count)].append(s)
            else:
                ans[tuple(count)] = [s]
        return ans.values()
        
        '''
        {
            eat: [eat, tea, ate]
            tan: [nat, tan]
            bat: [bat]
        }
        
        iterate through the input list,
        check if each word matches with any key in the dict
        if yes, append the word to the value of the key
        if not, add a new key and append this value
        * need a check anagram function
        iterate through the dicitonary and append all the values
        '''
