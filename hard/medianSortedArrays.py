from statistics import median
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        len1 = len(nums1)
        len2 = len(nums2)
        
        if len1 == 0:
            return median(nums2)
        
        if len2 == 0:
            return median(nums1)
        
        totalLength = len1 + len2
        
        medianLength = totalLength // 2  + 1
        
        i = 0
        
        resArray = []
        
        while i < medianLength:
            if len(nums1) > 0 and len(nums2) > 0:
                val = nums1.pop(0) if nums1[0] <= nums2[0] else nums2.pop(0)
                resArray.append(val)
            elif len(nums1) == 0:
                resArray.append(nums2.pop(0))
            else:
                resArray.append(nums1.pop(0))
            i += 1
        
        if totalLength % 2 == 0:
            return (resArray[-1] + resArray[-2]) / 2
        else:
            return resArray[-1]