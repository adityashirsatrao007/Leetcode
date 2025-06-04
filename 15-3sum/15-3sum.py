# Last updated: 6/4/2025, 9:24:11 PM
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Sort the array to use the two-pointer approach
        nums.sort()
        result = []
        
        for i in range(len(nums) - 2):
            # Avoid duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Use two pointers to find the other two elements
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    # Avoid duplicates for the second and third elements
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        
        return result

# Example usage
solution = Solution()
nums1 = [-1, 0, 1, 2, -1, -4]
nums2 = [0, 1, 1]
nums3 = [0, 0, 0]

print(solution.threeSum(nums1))  # Output: [[-1, -1, 2], [-1, 0, 1]]
print(solution.threeSum(nums2))  # Output: []
print(solution.threeSum(nums3))  # Output: [[0, 0, 0]]
