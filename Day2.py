# Day 2 - LeetCode Problems

# 1365. How Many Numbers Are Smaller Than the Current Number
# Given the array nums, for each nums[i] find out how many numbers in the array
# are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

from ast import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        # sort the nums and store in temp list
        temp = sorted(nums)
        # create a dictionary to store the number and its result(numbers smaller than it)
        d = {}

        # index is the number of the numbers smaller than it {num:res}
        for idx,val in enumerate(temp):
            if val not in d:
                d[val] = idx
        
        res = []
        for num in nums:
            res.append(d[num])
        
        return res

# Solution:
# Sort the array to determine the order of numbers.
# Use a dictionary to map each number to its index in the sorted array, which represents how many numbers are smaller than it.
# Finally, construct the result list by looking up each number in the dictionary.
# This approach has a time complexity of O(n log n) due to sorting.
# Space complexity is O(n) for the dictionary and result list.

# Note: check the duplicates in the sorted array to avoid overwriting the count for the same number.


# 1266. Minimum Time Visiting All Points
# On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # from one point to another
        # the minimum time is the larger value of the absolute difference between x and y

        total_time = 0
        for i in range(1,len(points)):
            x_diff = abs(points[i][0] - points[i-1][0])
            y_diff = abs(points[i][1] - points[i-1][1])
            min_time = max(x_diff,y_diff)
            total_time += min_time
        
        return total_time

# Solution:
# Iterate through each consecutive pair of points.
# For each pair, calculate the absolute differences in x and y coordinates.
# The time to move from one point to another is determined by the larger of these two differences
# (since diagonal movement is allowed).
# Sum these times to get the total time to visit all points.
# This approach has a time complexity of O(n), where n is the number of points.

# Another solution using while loop to simulate the movement step by step
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0

        x1,y1 = points.pop()
        while points:
            x2,y2 = points.pop()
            res += max(abs(x2-x1),abs(y2-y1))
            x1,y1 = x2,y2
        return res

# 54. Spiral Matrix
# Given an m x n matrix, return all elements of the matrix in spiral order.

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        while matrix:

            #1) add the first row
            res += matrix.pop(0)

            #2) add the last element of the rows
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            
            # 3) add the reversed elements of last row
            if matrix:
                res += matrix.pop()[::-1]
                    
            # 4) add the reverse order of the first element in row
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        
        return res
# Solution:
# Use a while loop to continuously extract the outer layers of the matrix.
# In each iteration, perform the following steps:
# 1) Remove and add the first row to the result.
# 2) Remove and add the last element of each remaining row.
# 3) Remove and add the last row in reverse order.
# 4) Remove and add the first element of each remaining row in reverse order.
# Repeat until the matrix is empty.
# This approach has a time complexity of O(m*n), where m and n are the dimensions of the matrix.

# Note: Check if the matrix and its rows are not empty before performing operations to avoid index errors.
# This is especially important for matrices with odd dimensions where the center element may be reached.

# Another solution using boundaries
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Pointer-based solution

        res = []
        rows, cols = len(matrix), len(matrix[0])

        top, bottom = 0, rows - 1
        left, right = 0, cols - 1

        while top <= bottom and left <= right:
            #1) left -> right accross the top row:
            for col in range(left,right+1):
                res.append(matrix[top][col])
            top += 1

            #2) top->bottom down the right column
            for row in range(top,bottom+1):
                res.append(matrix[row][right])
            right -= 1

            #3) right->left accross the bottom row (if still valid)
            if top <= bottom:
                for col in range(right,left-1,-1):
                    res.append(matrix[bottom][col])
                bottom -= 1
            
            #4) bottom -> top up the left column (if still valid)
            if left <= right:
                for row in range(bottom, top-1, -1):
                    res.append(matrix[row][left])
                left += 1
        
        return res
# Solution:
# Use four pointers to represent the current boundaries of the matrix: top, bottom, left, and right.
# In each iteration of the while loop, traverse the matrix in four directions:
# 1) From left to right across the top row.
# 2) From top to bottom down the right column.
# 3) From right to left across the bottom row (if the top boundary is still valid).
# 4) From bottom to top up the left column (if the left boundary is still valid).
# After each traversal, adjust the corresponding boundary inward.
# Repeat until the boundaries converge.
# This approach has a time complexity of O(m*n), where m and n are the dimensions of the matrix.    
# Note: Check the validity of the boundaries before traversing the bottom row and left column to avoid duplicates in cases of single-row or single-column remaining.

