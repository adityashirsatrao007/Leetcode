# Last updated: 6/4/2025, 9:22:44 PM
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word
    
    def search(self, word: str) -> str:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node.word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not words:
            return []
        
        # Initialize the Trie and insert all words into it
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        result = set()
        
        # Define the directions for moving in the board (right, left, down, up)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Backtracking function to explore the board
        def backtrack(x, y, node):
            if node.word:
                result.add(node.word)
                # Don't return to continue finding other words that start with the same prefix
            
            # Mark as visited
            visited[x][y] = True
            
            # Explore neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    next_char = board[nx][ny]
                    if next_char in node.children:
                        backtrack(nx, ny, node.children[next_char])
            
            # Backtrack: mark as not visited
            visited[x][y] = False
        
        # Start DFS/backtracking from each cell in the board
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie.root.children:
                    backtrack(i, j, trie.root.children[board[i][j]])
        
        return list(result)
