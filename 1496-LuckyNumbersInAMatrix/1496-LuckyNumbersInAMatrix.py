# Last updated: 6/4/2025, 9:20:28 PM
class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        min_in_row = {min(row) for row in matrix}
        max_in_column = {max(col) for col in zip(*matrix)}
        return list(min_in_row & max_in_column)

# Example usage:
sol = Solution()

matrix1 = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
matrix2 = [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]
matrix3 = [[7, 8], [1, 2]]

print(sol.luckyNumbers(matrix1))  # Output: [15]
print(sol.luckyNumbers(matrix2))  # Output: [12]
print(sol.luckyNumbers(matrix3))  # Output: [7]
