# Day 4 - 3 LeetCode Problems
from collections import deque
from typing import List

# 121. Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Two Pointer
        # L = buy , R = sell
        # find the min price to buy
        # buy low, sell high

        l,r = 0, 1
        max_profit = 0

        while r < len(prices):
            # if it's profitable
            if prices[l] < prices[r]:
                max_profit = max(max_profit, prices[r]-prices[l])
            else:
                l = r
            r += 1
        
        return max_profit

# Solution:
# Use two pointers to track the buying and selling days.
# Move the buying pointer to the right whenever a lower price is found.
# Calculate the profit whenever a higher selling price is found and update the maximum profit accordingly.
# Big O time complexity is O(n), where n is the number of days. Space complexity is O(1).

# 977. Squares of a Sorted Array
# Given an integer array nums sorted in non-decreasing order, return an array of the squares
# of each number sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # two pointer
        l,r = 0, len(nums)-1
        res = deque()

        while l <= r:
            left_sq, right_sq = nums[l]*nums[l], nums[r]*nums[r]
            if left_sq < right_sq:
                res.appendleft(right_sq)
                r -= 1
            else:
                res.appendleft(left_sq)
                l += 1
        
        return list(res)

# Solution:
# Use two pointers to compare the squares of the elements from both ends of the array.
# Append the larger square to the front of a deque and move the corresponding pointer inward.
# Convert the deque to a list before returning.
# Big O time complexity is O(n), where n is the number of elements in the array. Space complexity is O(n) for the output array.


# 15. 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that
# i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # sort the list
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            # skip duplicates
            if i>0 and nums[i] == nums[i-1]:
                continue

            l, r = i+1, n-1
            while l < r:
                total = nums[l] + nums[r] + nums[i]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[l],nums[r],nums[i]])
                    l += 1
                    # skip duplicates
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                
        return res

# Solution:
# Sort the array to facilitate the two-pointer technique.
# Iterate through the array, using each element as a potential first element of a triplet.
# For each first element, use two pointers to find pairs that sum to the negative of the first element.
# Skip duplicates to ensure unique triplets.
# Big O time complexity is O(n^2), where n is the number of elements in the array. Space complexity is O(k), where k is the number of unique triplets found.