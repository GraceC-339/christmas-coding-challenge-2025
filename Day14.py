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
    