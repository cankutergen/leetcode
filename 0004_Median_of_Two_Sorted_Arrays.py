class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        pointer_1 = 0
        pointer_2 = 0
        merged = []
        
        while pointer_1 < len(nums1) and pointer_2 < len(nums2):
            if nums1[pointer_1] < nums2[pointer_2]:
                merged.append(nums1[pointer_1])
                pointer_1 += 1
            else:
                merged.append(nums2[pointer_2])
                pointer_2 += 1

        while pointer_1 < len(nums1):
            merged.append(nums1[pointer_1])
            pointer_1 += 1

        while pointer_2 < len(nums2):
            merged.append(nums2[pointer_2])
            pointer_2 += 1

        return median(merged)
