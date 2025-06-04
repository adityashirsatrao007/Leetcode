# Last updated: 6/4/2025, 9:21:56 PM
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search_shortest_root(self, word):
        node = self.root
        prefix = ""
        for char in word:
            if char not in node.children:
                break
            node = node.children[char]
            prefix += char
            if node.is_end:
                return prefix
        return word

class Solution:
    def replaceWords(self, dictionary, sentence):
        trie = Trie()
        for root in dictionary:
            trie.insert(root)
        
        words = sentence.split()
        for i in range(len(words)):
            words[i] = trie.search_shortest_root(words[i])
        
        return " ".join(words)

# Example usage:
solution = Solution()
print(solution.replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"))  # Output: "the cat was rat by the bat"
print(solution.replaceWords(["a","b","c"], "aadsfasf absbs bbab cadsfafs"))  # Output: "a a b c"
