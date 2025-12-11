#LeetCode - Dynamic Programming

# 509. Fibonacci Number
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

# Naive Recursive Solution
def fib(n: int) -> int:
    if n <= 1:
        return n
    x = fib(n - 1)
    y = fib(n - 2)

    return x + y

n = 4
print(fib(n))

# Dynamic Programming Solution
def fib_dp(n: int) -> int:
    if n<= 1:
        return n
    
    dp = [0] * (n+1)
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

# Time Complexity: O(n)
# Space Complexity: O(n)

# 303. Range Sum Query - Immutable
# Given an integer array nums, handle multiple queries of the following type:
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
from typing import List
class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = [0]
        for n in nums:
            self.prefix.append(self.prefix[-1] + n)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]

# Solution:
# We use a prefix sum array to store the cumulative sums of the input array.
# This allows us to calculate the sum of any subarray in constant time.
# Time Complexity: O(1) for each sumRange query after O(n) preprocessing time
# Space Complexity: O(n) for the prefix sum array

