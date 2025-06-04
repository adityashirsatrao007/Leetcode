# Last updated: 6/4/2025, 9:23:59 PM
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while True:
            # Check if there are k nodes left
            start = prev.next
            end = prev
            for i in range(k):
                end = end.next
                if not end:
                    return dummy.next  # Less than k nodes left
            
            # Reverse the group of k nodes
            next_group = end.next
            end.next = None  # Disconnect the end of the current group
            
            prev.next = self.reverseList(start)  # Reverse the current group
            
            # Reconnect the reversed group
            start.next = next_group
            prev = start
        
        return dummy.next
    
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
