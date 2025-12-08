##  Leetcode - Sliding Window
# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/
# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr]
# of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

from ast import List

class MinSubArraySolution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        l = 0
        curr_sum = 0
        
        for r in range(len(nums)):
            curr_sum += nums[r]

            while curr_sum >= target:
                min_len = min(min_len, r-l+1)
                curr_sum -= nums[l]
                l += 1
        
        return min_len if min_len != float('inf') else 0
    
# Solution:
# We use a sliding window approach where we expand the right pointer to increase the sum
# and contract the left pointer to find the minimal length subarray that meets or exceeds the target.
# Time Complexity: O(n) where n is the length of nums
# Space Complexity: O(1)    

# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string s, find the length of the longest substring without repeating characters.
class LongestSubstringSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        sub_set = set() #checking duplicates
        max_len = 0

        for r in range(len(s)):
            while s[r] in sub_set:
                sub_set.remove(s[l])
                l += 1

            sub_set.add(s[r])
            max_len = max(max_len, r-l+1)
        
        return max_len

# Solution:
# We use a sliding window approach with two pointers and a set to track characters in the current substring.
# When we encounter a duplicate character, we move the left pointer to shrink the window until the duplicate is removed.
# Time Complexity: O(n) where n is the length of s
# Space Complexity: O(min(m, n)) where m is the size of the character set and n is the length of s

#Test Cases
if __name__ == "__main__":
    # Test for Minimum Size Subarray Sum
    min_subarray_solution = MinSubArraySolution()
    print(min_subarray_solution.minSubArrayLen(7, [2,3,1,2,4,3]))  # Expected output: 2
    print(min_subarray_solution.minSubArrayLen(4, [1,4,4]))        # Expected output: 1
    print(min_subarray_solution.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))  # Expected output: 0

    # Test for Longest Substring Without Repeating Characters
    longest_substring_solution = LongestSubstringSolution()
    print(longest_substring_solution.lengthOfLongestSubstring("abcabcbb"))  # Expected output: 3
    print(longest_substring_solution.lengthOfLongestSubstring("bbbbb"))     # Expected output: 1
    print(longest_substring_solution.lengthOfLongestSubstring("pwwkew"))    # Expected output: 3