# LeetCode
# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/
# Merge two sorted linked lists and return it as a new sorted list.
# The new list should be made by splicing together the nodes of the first two lists.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MergeTwoSortedListsSolution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        l1 = list1
        l2 = list2
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        tail.next = l1 if l1 else l2

        return dummy.next
# Solution:
# The solution uses a dummy node to simplify the merging process.
# It maintains two pointers, l1 and l2, to traverse the input lists.
# It compares the values at these pointers and appends the smaller value to the merged list.
# The process continues until one of the lists is fully traversed.
# Finally, it appends any remaining nodes from the non-empty list to the merged list.
# Time Complexity: O(n + m), where n and m are the lengths of the two linked lists.
# Space Complexity: O(1), as we are using only a constant amount of extra space for the dummy node and pointers.

