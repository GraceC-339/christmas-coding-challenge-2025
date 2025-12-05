# 845. Longest Mountain in Array
# https://leetcode.com/problems/longest-mountain-in-array/

# Given an integer array arr, return the length of the longest subarray, which is a mountain. 
# Return 0 if there is no mountain subarray.
# A mountain subarray is defined as a subarray that:
# - has at least 3 elements.
# - There exists some index i (0 < i < arr.length - 1) such that:
#   - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#   - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

from ast import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        # find the peak first and send left and right pointer to find the length of the mountain
        res = 0

        for i in range(1,len(arr)-1):
            if arr[i-1] < arr[i] > arr[i+1]:
                l = r = i

                while l > 0 and arr[l-1] < arr[l]:
                    l -= 1
                
                while r < len(arr)-1 and arr[r] > arr[r+1]:
                    r += 1
                
                res = max (res, r-l+1)
        
        return res

# Solution:
# The solution iterates through the array to find potential peaks of mountains.
# For each peak found, it expands left and right to determine the full length of the mountain.
# The maximum length of all mountains found is returned as the result.  
# The time complexity is O(n^2) in the worst case, where n is the length of the array,
# since for each peak we may need to traverse the entire array to find the left and right boundaries.   
# The space complexity is O(1) since we are using only a constant amount of extra space.


