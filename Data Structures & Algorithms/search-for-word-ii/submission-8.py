class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS, COLS = len(board), len(board[0])
        words = set(words)
        res = set()
        trie = Trie()

        for word in words:
            trie.insert(word)

        def dfs(r, c, visited, word, curr):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited or board[r][c] not in curr.children:
                return

            visited.add((r, c))

            curr = curr.children[board[r][c]]
            word += board[r][c]

            if curr.endOfWord:
                res.add(word)

            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, word, curr)
            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                visited = set()
                dfs(r, c, visited, "", trie.root)
        
        return list(res)

        