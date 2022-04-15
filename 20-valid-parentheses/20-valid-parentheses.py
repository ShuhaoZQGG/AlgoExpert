class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {'(': ')', '{':'}','[':']'}
        stack = []
        for c in s:
          if c in hashmap:
            stack.append(hashmap[c])
          else:
            if len(stack) > 0:
              if c == stack.pop():
                continue
              else:
                return False
            else:
              return False
        if len(stack) != 0:
          return False
        return True
                   