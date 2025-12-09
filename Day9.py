# LeetCode
# 136. Single Number
# Bit Manipulation
# https://leetcode.com/problems/single-number/
# Given a non-empty array of integers nums, every element appears twice except for one. Find the single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

from ast import List
class SingleNumerSolution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res

# Solution:
# We use the XOR bitwise operation which has the property that a ^ a = 0 and a ^ 0 = a.
# Thus, all numbers that appear twice will cancel each other out, leaving only the single number.
# Time Complexity: O(n) where n is the length of nums
# Space Complexity: O(1)

# 322. Coin Change
# Dynamic Programming
# https://leetcode.com/problems/coin-change/
# You are given an integer array coins representing coins of different denominations and an integer amount representing
# a total amount of money. Return the fewest number of coins that you need to make up that amount. If that amount of money
# cannot be made up by any combination of the coins, return -1. You may assume that you have an infinite number of each kind of coin.
class CoinChangeSolution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
        
        return dp[amount] if dp[amount] != amount + 1 else -1
    
# Solution:
# We use dynamic programming to build up a solution for the amount from 0 to the target amount.
# We initialize a dp array where dp[i] represents the minimum number of coins needed to make amount i.
# For each amount, we check each coin and update the dp array accordingly.
# Time Complexity: O(n * m) where n is the amount and m is the number of coins
# Space Complexity: O(n)

# 53. Maximum Subarray
# Dynamic Programming
# https://leetcode.com/problems/maximum-subarray/
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
class MaxSubArraySolution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        curr_sum = 0

        for num in nums:
            curr_sum += num
            max_sum = max(max_sum, curr_sum)
            if curr_sum < 0:
                curr_sum = 0

        return max_sum
# Solution:
# We iterate through the array, maintaining a current sum of the subarray.
# If the current sum becomes negative, we reset it to zero since starting a new subarray would be more beneficial.
# We keep track of the maximum sum encountered during the iteration.
# Time Complexity: O(n) where n is the length of nums
# Space Complexity: O(1)