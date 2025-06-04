# Last updated: 6/4/2025, 9:21:24 PM
class Solution(object):
    def minKBitFlips(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        flip = 0
        is_flipped = [0] * n
        result = 0
        
        for i in range(n):
            if i >= k:
                flip ^= is_flipped[i - k]
            
            if nums[i] == flip:
                if i + k > n:
                    return -1
                flip ^= 1
                is_flipped[i] = 1
                result += 1
        
        return result