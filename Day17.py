# Leetcode
# 203. Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/
# Remove all elements from a linked list of integers that have value val.
# Definition for singly-linked list.
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

