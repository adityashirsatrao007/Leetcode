# Last updated: 6/4/2025, 9:23:35 PM
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def create_board(state):
            board = []
            for row in state:
                board.append("".join(row))
            return board

        def backtrack(row):
            if row == n:
                result.append(create_board(board))
                return

            for col in range(n):
                if col in cols or (row + col) in diag1 or (row - col) in diag2:
                    continue

                cols.add(col)
                diag1.add(row + col)
                diag2.add(row - col)
                board[row][col] = 'Q'

                backtrack(row + 1)

                cols.remove(col)
                diag1.remove(row + col)
                diag2.remove(row - col)
                board[row][col] = '.'

        result = []
        cols = set()
        diag1 = set()
        diag2 = set()
        board = [["."] * n for _ in range(n)]

        backtrack(0)
        return result
