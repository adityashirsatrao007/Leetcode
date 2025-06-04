# Last updated: 6/4/2025, 9:17:58 PM
class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_seq_sum = 0
        current_sum = 0
        
        for i in range(len(nums)):
            if i == 0 or nums[i] == nums[i-1] + 1:
                current_sum += nums[i]
            else:
                break
        longest_seq_sum = current_sum
        
        missing = longest_seq_sum
        nums_set = set(nums)
        
        while missing in nums_set:
            missing += 1
        
        return missing
