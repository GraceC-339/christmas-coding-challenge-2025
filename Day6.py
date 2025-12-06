# 219. Contains Duplicate II
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j 
# in the array such that nums[i] == nums[j] and abs(i - j) <= k.
from ast import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # use hash set for a window of k
        window = set()

        for idx, val in enumerate(nums):
            if val in window:
                return True
            
            window.add(val)

            if len(window) > k:
                window.remove(nums[idx-k])
            
        return False

# Solution:
# Use a sliding window approach with a hash set to keep track of the last k elements.
# Iterate through the array, adding each element to the set.
# If an element is already in the set, return True.
# If the size of the set exceeds k, remove the oldest element (nums[idx - k]).
# If no duplicates are found within the k distance, return False.
# Time Complexity: O(n)
# Space Complexity: O(min(n, k))
