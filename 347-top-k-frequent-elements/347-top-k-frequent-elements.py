class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = dict()
        for num in nums:
          if num not in hashmap:
            hashmap[num] = 0
          hashmap[num] += 1
        res = []
        for k, v in sorted(hashmap.items(), key=lambda item:item[1], reverse = True)[:k]:
          res.append(k)
          
        return res

          