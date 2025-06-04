# Last updated: 6/4/2025, 9:21:35 PM
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.merge_sort(nums)
    
    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums

        # Divide the array into two halves
        mid = len(nums) // 2
        left_half = nums[:mid]
        right_half = nums[mid:]

        # Recursively sort each half
        left_sorted = self.merge_sort(left_half)
        right_sorted = self.merge_sort(right_half)

        # Merge the sorted halves
        return self.merge(left_sorted, right_sorted)

    def merge(self, left, right):
        sorted_array = []
        i = j = 0

        # Merge the two sorted arrays
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1

        # Append any remaining elements from the left or right array
        sorted_array.extend(left[i:])
        sorted_array.extend(right[j:])

        return sorted_array

# Example usage
solution = Solution()
nums1 = [5, 2, 3, 1]
nums2 = [5, 1, 1, 2, 0, 0]

print(solution.sortArray(nums1))  # Output: [1, 2, 3, 5]
print(solution.sortArray(nums2))  # Output: [0, 0, 1, 1, 2, 5]
