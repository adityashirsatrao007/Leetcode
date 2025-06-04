# Last updated: 6/4/2025, 9:19:22 PM
class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        def maxConsecutiveChar(ch):
            left = 0
            max_count = 0
            count = 0
            
            for right in range(len(answerKey)):
                if answerKey[right] != ch:
                    count += 1
                
                while count > k:
                    if answerKey[left] != ch:
                        count -= 1
                    left += 1
                
                max_count = max(max_count, right - left + 1)
            
            return max_count
        
        return max(maxConsecutiveChar('T'), maxConsecutiveChar('F'))

# Example usage
solution = Solution()
print(solution.maxConsecutiveAnswers("TTFF", 2))  # Output: 4
print(solution.maxConsecutiveAnswers("TFFT", 1))  # Output: 3
print(solution.maxConsecutiveAnswers("TTFTTFTT", 1))  # Output: 5
