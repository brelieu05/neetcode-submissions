class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(total, i, currentList):
            if total == target:
                res.append(currentList.copy())
                return
                
            if total > target or i >= len(candidates):
                return

                
            currentList.append(candidates[i])
            dfs(total + candidates[i], i + 1, currentList)
            currentList.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(total, i + 1, currentList)

        dfs(0, 0, [])
        return res