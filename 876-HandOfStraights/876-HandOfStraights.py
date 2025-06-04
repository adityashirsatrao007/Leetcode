# Last updated: 6/4/2025, 9:21:44 PM
from collections import Counter
import heapq

class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)
        
        while min_heap:
            min_card = min_heap[0]
            for i in range(min_card, min_card + groupSize):
                if count[i] == 0:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
                    
        return True

# Test cases
solution = Solution()
print(solution.isNStraightHand([1,2,3,6,2,3,4,7,8], 3))  # Output: True
print(solution.isNStraightHand([1,2,3,4,5], 4))           # Output: False
