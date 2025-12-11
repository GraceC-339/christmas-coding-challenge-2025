# Leetcode
# 338. Counting Bits
# https://leetcode.com/problems/counting-bits/
# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in
# the binary representation of i.
from typing import List 

class CountingBitsSolution:
    def countBits(self, n:int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
            
        return dp

# Solution:
# We use dynamic programming to build the solution iteratively.
# The number of 1's in the binary representation of a number i can be derived from the number of 1's in the number i - offset,
# where offset is the largest power of 2 less than or equal to i.
# Time Complexity: O(n) where n is the input number
# Space Complexity: O(n) for the output array
    