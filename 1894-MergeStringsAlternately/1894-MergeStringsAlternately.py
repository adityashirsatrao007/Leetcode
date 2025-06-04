# Last updated: 6/4/2025, 9:19:36 PM
class Solution:
    def mergeAlternately(self, word1, word2):
        # Initialize an empty list to store the characters of the merged string
        merged = []
        
        # Iterate through both strings simultaneously
        i = 0
        while i < len(word1) and i < len(word2):
            merged.append(word1[i])
            merged.append(word2[i])
            i += 1
        
        # Append any remaining characters from word1
        if i < len(word1):
            merged.extend(word1[i:])
        
        # Append any remaining characters from word2
        if i < len(word2):
            merged.extend(word2[i:])
        
        # Convert the list to a string and return it
        return ''.join(merged)

# Test cases
solution = Solution()
print(solution.mergeAlternately("abc", "pqr"))   # Output: "apbqcr"
print(solution.mergeAlternately("ab", "pqrs"))   # Output: "apbqrs"
print(solution.mergeAlternately("abcd", "pq"))   # Output: "apbqcd"
