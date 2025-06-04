# Last updated: 6/4/2025, 9:21:05 PM
from collections import Counter

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        # Step 1: Count the occurrences of each element in arr1
        count = Counter(arr1)
        
        # Step 2: Initialize the result list
        result = []
        
        # Step 3: Add elements from arr2 in the order specified by arr2
        for num in arr2:
            result.extend([num] * count[num])
            del count[num]  # Remove the element from the counter once processed
        
        # Step 4: Add remaining elements that are not in arr2, sorted in ascending order
        remaining_elements = sorted(count.elements())
        result.extend(remaining_elements)
        
        return result

# Example usage:
solution = Solution()
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
print(solution.relativeSortArray(arr1, arr2))  # Output: [2,2,2,1,4,3,3,9,6,7,19]

arr1 = [28,6,22,8,44,17]
arr2 = [22,28,8,6]
print(solution.relativeSortArray(arr1, arr2))  # Output: [22,28,8,6,17,44]
