# Last updated: 6/4/2025, 9:18:49 PM
class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        num_set = set(nums)
        count = 0
        
        for num in nums:
            if (num + diff in num_set) and (num + 2 * diff in num_set):
                count += 1
        
        return count
