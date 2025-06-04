# Last updated: 6/4/2025, 9:18:35 PM
class Solution(object):
    def unequalTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        count = Counter(nums)
        unique_nums = list(count.keys())
        num_unique = len(unique_nums)
        
        triplets = 0
        total = len(nums)
        
        for i in range(num_unique):
            for j in range(i + 1, num_unique):
                for k in range(j + 1, num_unique):
                    x, y, z = unique_nums[i], unique_nums[j], unique_nums[k]
                    triplets += (count[x] * count[y] * count[z])
        
        return triplets
