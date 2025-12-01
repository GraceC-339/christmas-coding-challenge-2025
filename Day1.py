# Day 1
# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.  

from ast import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,v in enumerate(nums):
            if target - v in seen:
                return [i, seen[target-v]]
            seen[v] = i

# Solution: Use hash map to store seen numbers and their indices.
# For each number, check if the complement (target - current number) exists in the hash map.
# If it exists, return the indices. This approach has a time complexity of O(n).



