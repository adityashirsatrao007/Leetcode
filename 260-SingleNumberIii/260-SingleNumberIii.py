# Last updated: 6/4/2025, 9:22:32 PM
class Solution:
    def singleNumber(self, nums):
        # Step 1: XOR all the numbers
        xor_all = 0
        for num in nums:
            xor_all ^= num
        
        # Step 2: Find a differentiating bit (rightmost set bit)
        diff_bit = xor_all & -xor_all
        
        # Step 3: Divide numbers into two groups and XOR within each group
        num1, num2 = 0, 0
        for num in nums:
            if num & diff_bit:
                num1 ^= num
            else:
                num2 ^= num
        
        return [num1, num2]

# Example usage
sol = Solution()
nums1 = [1, 2, 1, 3, 2, 5]
nums2 = [-1, 0]
nums3 = [0, 1]

print(sol.singleNumber(nums1))  # Output: [3, 5] or [5, 3]
print(sol.singleNumber(nums2))  # Output: [-1, 0]
print(sol.singleNumber(nums3))  # Output: [1, 0] or [0, 1]
