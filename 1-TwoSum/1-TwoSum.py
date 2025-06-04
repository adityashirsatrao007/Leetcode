# Last updated: 6/4/2025, 9:24:40 PM
class Solution:
    def twoSum(self, nums, target):
        num_indices = {}  # Map to store the complement and its index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_indices:
                return [num_indices[complement], i]
            num_indices[num] = i

# Example usage:
def _driver():
    sol = Solution()
    
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = sol.twoSum(nums1, target1)
    print("Output 1: {}".format(result1))

    nums2 = [3, 2, 4]
    target2 = 6
    result2 = sol.twoSum(nums2, target2)
    print("Output 2: {}".format(result2))

    nums3 = [3, 3]
    target3 = 6
    result3 = sol.twoSum(nums3, target3)
    print("Output 3: {}".format(result3))

if __name__ == "__main__":
    _driver()
