# Last updated: 6/4/2025, 9:23:31 PM
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def backtrack(row, diagonals, antiDiagonals, cols):
            if row == n:
                return 1
            
            solutions = 0
            for col in range(n):
                currDiagonal = row - col
                currAntiDiagonal = row + col
                
                if col in cols or currDiagonal in diagonals or currAntiDiagonal in antiDiagonals:
                    continue
                
                cols.add(col)
                diagonals.add(currDiagonal)
                antiDiagonals.add(currAntiDiagonal)
                
                solutions += backtrack(row + 1, diagonals, antiDiagonals, cols)
                
                cols.remove(col)
                diagonals.remove(currDiagonal)
                antiDiagonals.remove(currAntiDiagonal)
            
            return solutions
        
        return backtrack(0, set(), set(), set())

# Example usage:
solution = Solution()
print(solution.totalNQueens(4))  # Output: 2
print(solution.totalNQueens(1))  # Output: 1
