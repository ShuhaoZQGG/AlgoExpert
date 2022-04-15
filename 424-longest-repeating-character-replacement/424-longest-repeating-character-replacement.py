class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        subString = ''
        counter = 0
        hashmap = dict()
        while left < len(s) and right < len(s):
          if s[right] not in hashmap:
            hashmap[s[right]] = 0
          hashmap[s[right]] += 1
          subString += s[right]
          maxHash = max(hashmap, key=hashmap.get)
          if len(subString) - hashmap[maxHash] > k:
            subString = subString[1:]
            hashmap[s[left]] -= 1
            left += 1
          right += 1
          counter = max(len(subString),counter)

        return counter
            
          