# Last updated: 6/4/2025, 9:17:48 PM
class Solution:
    def numberOfPairs(self, nums1, nums2, k):
        good_pair_count = 0
        for num1 in nums1:
            for num2 in nums2:
                if num1 % (num2 * k) == 0:
                    good_pair_count += 1
        return good_pair_count

# Testing the function with various test cases
if __name__ == "__main__":
    solution = Solution()

    # Example case 1
    nums1 = [1, 3, 4]
    nums2 = [1, 3, 4]
    k = 1
    print(solution.numberOfPairs(nums1, nums2, k))  # Expected output: 5

    # Example case 2
    nums1 = [1, 2, 4, 12]
    nums2 = [2, 4]
    k = 3
    print(solution.numberOfPairs(nums1, nums2, k))  # Expected output: 2

    # Minimal edge case
    nums1 = [1]
    nums2 = [1]
    k = 1
    print(solution.numberOfPairs(nums1, nums2, k))  # Expected output: 1

    # Case with no good pairs
    nums1 = [1, 1, 1]
    nums2 = [2, 2, 2]
    k = 1
    print(solution.numberOfPairs(nums1, nums2, k))  # Expected output: 0

    # Case with maximum values within constraints
    nums1 = [50] * 50
    nums2 = [1] * 50
    k = 50
    print(solution.numberOfPairs(nums1, nums2, k))  # Expected output: 50

    # Mixed case with some good pairs
    nums1 = [10, 15, 20, 30]
    nums2 = [1, 5, 10]
    k = 2
    print(solution.numberOfPairs(nums1, nums2, k))  # Expected output: 5

    # Additional test cases
    # Case with random values
    nums1 = [9, 18, 27]
    nums2 = [3, 6]
    k = 1
    print(solution.numberOfPairs(nums1, nums2, k))  # Expected output: 6

    # Case with k greater than elements in nums2
    nums1 = [12, 24, 36]
    nums2 = [2, 4]
    k = 10
    print(solution.numberOfPairs(nums1, nums2, k))  # Expected output: 0
