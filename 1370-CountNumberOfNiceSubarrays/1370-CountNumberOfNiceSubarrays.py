# Last updated: 6/4/2025, 9:20:44 PM
class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        prefix_sums = {0: 1}
        current_sum = 0

        for num in nums:
            if num % 2 == 1:
                current_sum += 1

            if current_sum - k in prefix_sums:
                count += prefix_sums[current_sum - k]

            if current_sum in prefix_sums:
                prefix_sums[current_sum] += 1
            else:
                prefix_sums[current_sum] = 1

        return count
