# Linked List
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

#206. Reverse Linked List
#https://leetcode.com/problems/reverse-linked-list/
#Given the head of a singly linked list, reverse the list, and return the reversed list
class ReverseLinkedListSolution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev


#876. Middle of the Linked List
#https://leetcode.com/problems/middle-of-the-linked-list/
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.



class MiddleLinkedListSolution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

#Solution:
# We use two pointers, slow and fast. The slow pointer moves one step at a time, while the fast pointer moves two steps.
# When the fast pointer reaches the end of the list, the slow pointer will be at the middle node.
# This approach ensures that if there are two middle nodes, 
# the slow pointer will point to the second one when the fast pointer reaches the end.        
# The time complexity is O(n) and the space complexity is O(1).

# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
# Return true if there is a cycle in the linked list. Otherwise, return false.

class LinkedListCycleSolution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True
        
        return False

#Solution:
# Similar to the previous problem, we use two pointers, slow and fast.
# The slow pointer moves one step at a time, while the fast pointer moves two steps.
# If there is a cycle, the fast pointer will eventually meet the slow pointer.
# If the fast pointer reaches the end of the list, there is no cycle.
# The time complexity is O(n) and the space complexity is O(1).

