#Leetcode
# 77. Combinations
# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# You may return the answer in any order.

from typing import List

class CombinationsSolution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, path):
            if len(path) == k:
                result.append(path[:])
                return
            for i in range(start,n+1):
                path.append(i)
                backtrack(i+1, path)
                path.pop()
        
        result = []
        backtrack(1,[])

        return result

# Solution:
# We use backtracking to explore all combinations. We start from a given number and build the
# combination by adding numbers sequentially until we reach the desired length k.
# Time Complexity: O(C(n, k) * k) where C(n, k)
# Space Complexity: O(k) for the recursion stack
