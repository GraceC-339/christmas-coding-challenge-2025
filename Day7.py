# LeetCode
# 1200. Minimum Absolute Difference
# https://leetcode.com/problems/minimum-absolute-difference/
# Given an array of distinct integers arr, 
# find all pairs of elements with the minimum absolute difference of any two elements.

from ast import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # sort the array
        arr.sort()

        min_diff = float('inf') 

        # find the minimum difference
        for i in range(1, len(arr)):
            abs_diff = abs(arr[i] - arr[i-1])
            min_diff = min(min_diff, abs_diff)
        
        res = []

        # find the pairs
        for i in range(1, len(arr)):
            if abs(arr[i] - arr[i-1]) == min_diff:
                res.append([arr[i-1], arr[i]])

        return res

# Solution:
# First, sort the array to bring elements with smaller differences closer together.
# Then, iterate through the sorted array to find the minimum absolute difference between consecutive elements.
# Finally, iterate again to collect all pairs of elements that have this minimum difference.
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(1) if we ignore the output list

