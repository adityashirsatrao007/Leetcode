# Last updated: 6/4/2025, 9:17:38 PM
class Solution(object):
    def getEncryptedString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)
        encrypted_string = []
        
        for i in range(n):
            # Find the kth character after the current character in a cyclic manner
            new_index = (i + k) % n
            encrypted_string.append(s[new_index])
        
        return ''.join(encrypted_string)

# Example usage:
solution = Solution()
print(solution.getEncryptedString("dart", 3))  # Output: "tdar"
print(solution.getEncryptedString("aaa", 1))   # Output: "aaa"
