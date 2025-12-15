# 46. Permutaions
# Given a collection of distinct integers, return all possible permutations. 
from typing import List

class PermutationsSolution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        perms = self.permute(nums[1:])
        result = []

        for perm in perms:
            for i in range(len(perm) + 1):
                copy_perm = perm.copy()
                copy_perm.insert(i, nums[0])
                result.append(copy_perm)
        
        return result

# Solution:
# We use recursion to generate permutations. For each number, we insert it into every possible
# position of the permutations generated from the remaining numbers.
# Time Complexity: O(n * n!) where n is the length of nums
# Space Complexity: O(n!) for storing all permutations