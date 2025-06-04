# Last updated: 6/4/2025, 9:21:10 PM
class Solution(object):
    def minHeightShelves(self, books, shelfWidth):
        """
        :type books: List[List[int]]
        :type shelfWidth: int
        :rtype: int
        """
        n = len(books)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            total_width = 0
            max_height = 0
            j = i
            while j > 0:
                total_width += books[j - 1][0]
                if total_width > shelfWidth:
                    break
                max_height = max(max_height, books[j - 1][1])
                dp[i] = min(dp[i], dp[j - 1] + max_height)
                j -= 1

        return dp[n]

# Example usage
solution = Solution()
books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
shelfWidth = 4
print(solution.minHeightShelves(books, shelfWidth))  # Output: 6

books = [[1,3],[2,4],[3,2]]
shelfWidth = 6
print(solution.minHeightShelves(books, shelfWidth))  # Output: 4
