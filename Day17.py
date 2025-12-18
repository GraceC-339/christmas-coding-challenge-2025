# Leetcode
# 203. Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/
# Remove all elements from a linked list of integers that have value val.
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class RemoveLinkedListElementsSolution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0, head)
        curr = dummy

        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return dummy.next

# Solution:
# The solution uses a dummy node to handle edge cases where the head node itself needs to be removed.
# It iterates through the linked list, checking each node's value.
# If a node's value matches the target value, it skips that node by adjusting the pointers.
# Finally, it returns the modified list starting from the node after the dummy node.    
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(1), as we are using only a constant amount of extra space
# for the dummy node and a pointer.

# 92. Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/
# Reverse a linked list from position m to n. Do it in one-pass.
class ReverseLinkedListIISolution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        #Traverse to find the left node
        left_prev, curr = dummy, head

        for _ in range(left-1):
            left_prev, curr = curr, curr.next
        
        # Reverse the sublist from left to right
        prev = None

        for _ in range(right - left + 1):
            next_node = curr.next
            curr.next = prev
            prev, curr = curr, next_node
        
        # Connect the reversed sublist back to the main list
        left_prev.next.next = curr
        left_prev.next = prev

        return dummy.next

# Solution:
# The solution uses a dummy node to simplify edge cases.
# It first traverses the list to find the node just before the left position.
# Then, it reverses the sublist from left to right using a standard linked list reversal technique.
# Finally, it reconnects the reversed sublist back to the main list.
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(1), as we are using only a constant amount of extra space
# for the dummy node and pointers.