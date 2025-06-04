# Last updated: 6/4/2025, 9:24:33 PM
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        total_size = len(nums1) + len(nums2)
        left, right = 0, len(nums1)

        while left <= right:
            partition_x = (left + right) // 2
            partition_y = (total_size + 1) // 2 - partition_x

            max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
            min_right_x = float('inf') if partition_x == len(nums1) else nums1[partition_x]
            max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
            min_right_y = float('inf') if partition_y == len(nums2) else nums2[partition_y]

            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if total_size % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2.0
                else:
                    return float(max(max_left_x, max_left_y))
            elif max_left_x > min_right_y:
                right = partition_x - 1
            else:
                left = partition_x + 1

        return -1  # Invalid input

# Example usage
nums1 = [1, 3]
nums2 = [2]
solution = Solution()
print(solution.findMedianSortedArrays(nums1, nums2))  # Output: 2.00000

nums3 = [1, 2]
nums4 = [3, 4]
print(solution.findMedianSortedArrays(nums3, nums4))  # Output: 2.50000
