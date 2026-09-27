class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def prefix(self, pre):
        curr = self.root
        for c in pre:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

    def check(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endOfWord


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        ROWS, COLS = len(board), len(board[0])
        res = set()
        visited = set()

        for word in words:
            trie.insert(word)

        def dfs(r, c, word, root):
            if (r >= ROWS or c >= COLS or r < 0 or c < 0 or (r, c) in visited):
                return
            
            word += board[r][c]
            if board[r][c] in root.children:
                root = root.children[board[r][c]]
            else:
                return

            if root.endOfWord:
                res.add(word)

            visited.add((r, c))

            dfs(r + 1, c, word, root)
            dfs(r - 1, c, word, root)
            dfs(r, c - 1, word, root)
            dfs(r, c + 1, word, root)

            visited.remove((r, c))


        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited:
                    dfs(r, c, "", trie.root)
                            
        return list(res)





        