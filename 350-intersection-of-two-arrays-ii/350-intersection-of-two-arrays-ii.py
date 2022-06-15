class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        if len(nums1) >= len(nums2):
            nums1, nums2 = nums1, nums2
        else:
            nums1, nums2 = nums2, nums1

        hm = dict()
        
        for i in range(len(nums1)):
            if nums1[i] not in hm:
                hm[nums1[i]] = 0
            hm[nums1[i]] += 1
        
        for i in range(len(nums2)):
            if nums2[i] in hm and hm[nums2[i]] > 0:
                hm[nums2[i]] -= 1
                res.append(nums2[i])
        return res