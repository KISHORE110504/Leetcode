"""Given an integer array nums, return the number of subarrays filled with 0.
A subarray is a contiguous non-empty sequence of elements within an array."""

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        total = 0

        for i in nums:
            if i == 0:
                count += 1
                total += count
            else:
                count = 0
        return total
