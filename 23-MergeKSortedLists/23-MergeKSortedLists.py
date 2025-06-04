# Last updated: 6/4/2025, 9:24:01 PM
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Create a min-heap
        min_heap = []
        
        # Push the first element of each linked list into the heap
        for head in lists:
            if head:
                heapq.heappush(min_heap, (head.val, head))
        
        # Dummy node to simplify the code
        dummy = ListNode(0)
        curr = dummy
        
        # While there are elements in the min-heap
        while min_heap:
            # Pop the smallest element
            val, node = heapq.heappop(min_heap)
            # Append the popped element to the result list
            curr.next = node
            curr = curr.next
            # Move to the next node in the popped linked list
            if node.next:
                heapq.heappush(min_heap, (node.next.val, node.next))
        
        return dummy.next
