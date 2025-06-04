# Last updated: 6/4/2025, 9:21:23 PM
from collections import Counter

class Solution:
    def commonChars(self, words):
        # Initialize the counter with the first word
        min_freq = Counter(words[0])
        
        # Update the counter with the minimum frequencies for each subsequent word
        for word in words[1:]:
            min_freq &= Counter(word)
        
        # Construct the result based on the minimum frequencies
        result = []
        for char, count in min_freq.items():
            result.extend([char] * count)
        
        return result

# Test cases
solution = Solution()
print(solution.commonChars(["bella", "label", "roller"]))  # Output: ["e", "l", "l"]
print(solution.commonChars(["cool", "lock", "cook"]))      # Output: ["c", "o"]
