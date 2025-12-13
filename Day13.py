# Leetcode
# 78. Subsets
# https://leetcode.com/problems/subsets/
# Given an integer array nums of unique elements, return all possible subsets (the power set).

from typing import List

class SubsetSolution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            # check base case
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)

            # decision to not include nums[i]
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res

# Solution:
# We use a depth-first search (DFS) approach to explore all possible subsets.
# At each index, we have two choices: include the current number in the subset or exclude it.
# We recursively explore both choices until we reach the end of the list, at which point we add the current subset to the result list.
# Time Complexity: O(2^n), where n is the number of elements in the input array.
# Space Complexity: O(n) for the recursion stack and the subset list. The output list will take O(2^n) spaces