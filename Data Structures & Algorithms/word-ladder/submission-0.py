class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        res = float('inf')
        visited = set()
        wordList = set(wordList)
        
        q = deque()
        q.append((beginWord, 1))
        visited.add(beginWord)

        while q:
            word, count = q.popleft()

            if word == endWord:
                res = min(res, count)

            for i in range(len(word)):
                for c in range(97, 123):
                    newWord = word[:i] + chr(c) + word[i+1:]
                    if newWord in wordList and newWord not in visited:
                        print(newWord)
                        q.append((newWord, count + 1))
                        visited.add(newWord)
            
        return 0 if res == float('inf') else res