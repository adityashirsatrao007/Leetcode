# Last updated: 6/4/2025, 9:22:58 PM
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # If mid element is greater than the right element, it means minimum is in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            # If mid element is less than the right element, it means minimum is in the left half
            elif nums[mid] < nums[right]:
                right = mid
            # If mid element is equal to the right element, we cannot decide which half to choose,
            # so decrement right by 1 to narrow down the search
            else:
                right -= 1
        
        return nums[left]
