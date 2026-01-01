class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_arr = nums1 + nums2
        merged_arr.sort()

        n = len(merged_arr)
        if n % 2 != 0:
            return float(merged_arr[n//2])
        else:
            mid1 = merged_arr[n//2]
            mid2 = merged_arr[(n//2) - 1]
            return (mid1 + mid2)/2.0
