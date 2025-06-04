# Last updated: 6/4/2025, 9:22:38 PM
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        result = []
        window = deque()
        
        for i in range(len(nums)):
            # Remove elements outside the window's range
            if window and window[0] <= i - k:
                window.popleft()
            
            # Maintain a decreasing deque for maximum values
            while window and nums[window[-1]] <= nums[i]:
                window.pop()
            
            window.append(i)
            
            # Add maximum element for the current window
            if i >= k - 1:
                result.append(nums[window[0]])
        
        return result
