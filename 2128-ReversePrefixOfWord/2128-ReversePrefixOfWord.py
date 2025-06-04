# Last updated: 6/4/2025, 9:19:24 PM
class Solution:
    def reversePrefix(self, word, ch):
        index = word.find(ch)
        if index != -1:
            return word[:index+1][::-1] + word[index+1:]
        return word

# Example usage:
solution = Solution()
print(solution.reversePrefix("abcdefd", "d"))  # Output: "dcbaefd"
print(solution.reversePrefix("xyxzxe", "z"))   # Output: "zxyxxe"
print(solution.reversePrefix("abcd", "z"))     # Output: "abcd"
