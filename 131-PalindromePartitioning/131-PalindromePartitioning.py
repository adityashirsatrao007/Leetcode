# Last updated: 6/4/2025, 9:23:10 PM
class Solution:
    def partition(self, s):
        def is_palindrome(string):
            return string == string[::-1]

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:end]):
                    path.append(s[start:end])
                    backtrack(end, path)
                    path.pop()

        result = []
        backtrack(0, [])
        return result

# Example usage:
solution = Solution()
print(solution.partition("aab"))  # Output: [["a","a","b"],["aa","b"]]
print(solution.partition("a"))    # Output: [["a"]]
