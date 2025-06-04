# Last updated: 6/4/2025, 9:21:26 PM
class Solution:
    def subarraysDivByK(self, nums, k):
        count = 0
        prefix_sum = 0
        remainder_count = {0: 1}  # We start with remainder 0 having one count for initial case

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            
            # Adjust remainder to be positive
            if remainder < 0:
                remainder += k

            # If this remainder has been seen before, it means there are subarrays which have sums divisible by k
            if remainder in remainder_count:
                count += remainder_count[remainder]
                remainder_count[remainder] += 1
            else:
                remainder_count[remainder] = 1

        return count

# Example usage:
# Example 1
nums1 = [4, 5, 0, -2, -3, 1]
k1 = 5
solution = Solution()
print(solution.subarraysDivByK(nums1, k1))  # Output: 7

# Example 2
nums2 = [5]
k2 = 9
print(solution.subarraysDivByK(nums2, k2))  # Output: 0
