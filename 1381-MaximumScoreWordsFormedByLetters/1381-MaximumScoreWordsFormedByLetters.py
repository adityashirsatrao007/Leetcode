# Last updated: 6/4/2025, 9:20:42 PM
class Solution:
    @staticmethod
    def maxScoreWords(words, letters, score):
        # Count frequency of each letter in letters
        letter_freq = {}
        for letter in letters:
            if letter in letter_freq:
                letter_freq[letter] += 1
            else:
                letter_freq[letter] = 1

        # Compute score of each word
        word_scores = [0] * len(words)
        for i, word in enumerate(words):
            for letter in word:
                word_scores[i] += score[ord(letter) - ord('a')]

        # Recursive function to find max score
        def dfs(index, remaining_letters):
            if index == len(words):
                return 0

            # Try including the current word
            word_score = word_scores[index]
            word_letter_freq = {}
            for letter in words[index]:
                if letter in word_letter_freq:
                    word_letter_freq[letter] += 1
                else:
                    word_letter_freq[letter] = 1

            can_include = True
            for letter, count in word_letter_freq.items():
                if letter not in remaining_letters or remaining_letters[letter] < count:
                    can_include = False
                    break

            max_score_include = 0
            if can_include:
                updated_letters = remaining_letters.copy()
                for letter, count in word_letter_freq.items():
                    updated_letters[letter] -= count
                max_score_include = word_score + dfs(index + 1, updated_letters)

            # Try excluding the current word
            max_score_exclude = dfs(index + 1, remaining_letters)

            return max(max_score_include, max_score_exclude)

        return dfs(0, letter_freq)

# Test cases
words1 = ["dog", "cat", "dad", "good"]
letters1 = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
score1 = [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(Solution().maxScoreWords(words1, letters1, score1))  # Output: 23

words2 = ["xxxz", "ax", "bx", "cx"]
letters2 = ["z", "a", "b", "c", "x", "x", "x"]
score2 = [4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 10]
print(Solution().maxScoreWords(words2, letters2, score2))  # Output: 27

words3 = ["leetcode"]
letters3 = ["l", "e", "t", "c", "o", "d"]
score3 = [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
print(Solution().maxScoreWords(words3, letters3, score3))  # Output: 0
