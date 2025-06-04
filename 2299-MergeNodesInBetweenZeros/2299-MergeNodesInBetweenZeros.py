# Last updated: 6/4/2025, 9:19:02 PM
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current = dummy
        sum_val = 0
        head = head.next  # Skip the initial zero
        
        while head:
            if head.val == 0:
                current.next = ListNode(sum_val)
                current = current.next
                sum_val = 0
            else:
                sum_val += head.val
            head = head.next
        
        return dummy.next
