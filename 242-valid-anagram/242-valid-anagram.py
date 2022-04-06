class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = dict()
        for c in s:
          if c not in hashmap:
            hashmap[c] = 0
          hashmap[c] += 1
        
        for k in t:
          if k in hashmap and hashmap[k] > 0:
            hashmap[k] -= 1
          else:
            return False
        
        for k, v in hashmap.items():
          if v != 0:
            return False
          
        return True
          