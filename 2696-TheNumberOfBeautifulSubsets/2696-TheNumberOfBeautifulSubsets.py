# Last updated: 6/4/2025, 9:18:14 PM
class Solution:
    def beautifulSubsets(self, nums, k):
        nums.sort()  # Sorting to facilitate easier checks
        n = len(nums)
        beautiful_count = [0]  # Use a list to hold the count

        def backtrack(index, current_subset):
            if index == n:
                if current_subset:
                    beautiful_count[0] += 1
                return

            # Check if we can include nums[index] in the current subset
            can_include = True
            for num in current_subset:
                if abs(num - nums[index]) == k:
                    can_include = False
                    break

            # If we can include nums[index], recurse with it included
            if can_include:
                current_subset.append(nums[index])
                backtrack(index + 1, current_subset)
                current_subset.pop()

            # Recurse without including nums[index]
            backtrack(index + 1, current_subset)

        # Start backtracking from the first index
        backtrack(0, [])

        return beautiful_count[0]

# Example Usage
solution = Solution()
print(solution.beautifulSubsets([2, 4, 6], 2))  # Output: 4
print(solution.beautifulSubsets([1], 1))  # Output: 1
