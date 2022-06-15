class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        longList, shortList = [], []
        if len(nums1) >= len(nums2):
            longList = nums1
            shortList = nums2
        else:
            longList = nums2
            shortList = nums1
        
        hm = dict()
        
        for i in range(len(longList)):
            if longList[i] not in hm:
                hm[longList[i]] = 0
            hm[longList[i]] += 1
        
        for i in range(len(shortList)):
            if shortList[i] in hm and hm[shortList[i]] > 0:
                hm[shortList[i]] -= 1
                res.append(shortList[i])
        return res