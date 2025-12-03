# Day 3
# LeetCode Problems

# 200. Number of Islands
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.    

from ast import List
import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # input validation
        if not grid:
            return 0
        
        # use bfs/dfs to vistit all the grid of an island
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))

            # explore the grid in different directions
            while q:
                row,col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    r,c = row+dr, col+dc
                    if (r in range(rows) and c in range(cols) and 
                        grid[r][c] == "1" and (r,c) not in visit):
                        visit.add((r,c))
                        q.append((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
        
        return islands

# Solution:
# Use BFS or DFS to explore each island in the grid.
# Maintain a set to track visited land cells.
# For each unvisited land cell, initiate a BFS/DFS to mark all connected land cells as visited.
# Increment the island count for each BFS/DFS initiation.
# The time complexity is O(m*n), where m and n are the dimensions of the grid.

# 26. Remove Duplicates from Sorted Array
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,r = 0, 1

        while r < len(nums):
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]
            r += 1
        
        return l+1

# Solution:
# Use two pointers to traverse the sorted array.
# The left pointer tracks the position of the last unique element found.
# The right pointer scans through the array.
# When a new unique element is found, increment the left pointer and update the value at that position.
# The time complexity is O(n), where n is the length of the array.

