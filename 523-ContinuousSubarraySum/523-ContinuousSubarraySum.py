# Last updated: 6/4/2025, 9:22:03 PM
class Solution:
    def checkSubarraySum(self, nums, k):
        # Edge case when k is zero
        if k == 0:
            # We need to find at least one pair of zeros
            for i in range(len(nums) - 1):
                if nums[i] == 0 and nums[i + 1] == 0:
                    return True
            return False

        # Dictionary to store the first occurrence of each modulo value
        mod_dict = {0: -1}  # To handle the case where the subarray starts from index 0
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            mod_value = prefix_sum % k
            
            if mod_value in mod_dict:
                if i - mod_dict[mod_value] > 1:
                    return True
            else:
                mod_dict[mod_value] = i
        
        return False

# Example usage:
solution = Solution()
print(solution.checkSubarraySum([23, 2, 4, 6, 7], 6))  # Output: True
print(solution.checkSubarraySum([23, 2, 6, 4, 7], 6))  # Output: True
print(solution.checkSubarraySum([23, 2, 6, 4, 7], 13)) # Output: False
