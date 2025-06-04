# Last updated: 6/4/2025, 9:20:19 PM
class Solution:
    def countTriplets(self, arr):
        n = len(arr)
        prefix = [0] * (n + 1)
        
        # Compute the prefix XOR array
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ arr[i]
        
        count = 0
        
        # Iterate over all pairs (i, k)
        for i in range(n):
            for k in range(i + 1, n):
                if prefix[i] == prefix[k + 1]:
                    # For each valid pair (i, k), we have (k - i) valid j values
                    count += (k - i)
        
        return count

# Example usage
sol = Solution()
arr1 = [2, 3, 1, 6, 7]
arr2 = [1, 1, 1, 1, 1]

print(sol.countTriplets(arr1))  # Output: 4
print(sol.countTriplets(arr2))  # Output: 10
