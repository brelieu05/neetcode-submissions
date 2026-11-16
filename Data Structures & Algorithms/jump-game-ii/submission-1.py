from functools import lru_cache

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        @lru_cache
        def dfs(i):
            if i == len(nums) - 1:
                return 0
            if i >= len(nums):
                return float('inf')


            curr = float('inf')
            for j in range(1, nums[i] + 1):
                curr = min(curr, 1 + dfs(i + j))
            return curr

        return dfs(0)