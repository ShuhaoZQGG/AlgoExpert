class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for string in strs:
          ans[''.join(sorted(string))].append(string)
        return ans.values()
       
