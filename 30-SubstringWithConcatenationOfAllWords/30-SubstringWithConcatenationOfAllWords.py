# Last updated: 6/4/2025, 9:23:51 PM
from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        
        word_length = len(words[0])
        total_length = len(words) * word_length
        word_count = Counter(words)
        result = []
        
        for i in range(len(s) - total_length + 1):
            substring = s[i:i+total_length]
            found_words = []
            for j in range(0, total_length, word_length):
                found_words.append(substring[j:j+word_length])
            
            found_count = Counter(found_words)
            
            if found_count == word_count:
                result.append(i)
        
        return result
