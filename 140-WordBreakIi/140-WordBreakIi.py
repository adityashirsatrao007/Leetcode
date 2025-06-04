# Last updated: 6/4/2025, 9:23:05 PM
class Solution:
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)  # Convert the list to a set for faster lookup
        memo = {}  # Dictionary to store the results of subproblems

        def backtrack(start):
            if start in memo:
                return memo[start]
            if start == len(s):
                return [""]

            sentences = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    for subsentence in backtrack(end):
                        if subsentence:
                            sentences.append(word + " " + subsentence)
                        else:
                            sentences.append(word)
            
            memo[start] = sentences
            return sentences
        
        return backtrack(0)

# Example usage
s1 = "catsanddog"
wordDict1 = ["cat", "cats", "and", "sand", "dog"]
solution = Solution()
print(solution.wordBreak(s1, wordDict1))  # Output: ["cats and dog", "cat sand dog"]

s2 = "pineapplepenapple"
wordDict2 = ["apple", "pen", "applepen", "pine", "pineapple"]
print(solution.wordBreak(s2, wordDict2))  # Output: ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]

s3 = "catsandog"
wordDict3 = ["cats", "dog", "sand", "and", "cat"]
print(solution.wordBreak(s3, wordDict3))  # Output: []
