# LeetCode
# 234. Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/
# Given the head of a singly linked list, return true if it is a palindrome.

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find the middle using fast and slow pointer
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse the second half
        prev = None
        while slow:
            next_pointer = slow.next
            slow.next = prev
            prev = slow
            slow = next_pointer
        # when it's end, prev = second half head
        # compare the two linked list
        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False
            
            left = left.next
            right = right.next
        
        return True

# Solution:
# The solution first finds the middle of the linked list using the fast and slow pointer technique.
# It then reverses the second half of the linked list in place.
# After reversing, it compares the first half and the reversed second half node by node.
# If all corresponding nodes match, the linked list is a palindrome; otherwise, it is not
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(1), as we are reversing the list in place and using only
# a constant amount of extra space for pointers.