class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()

        ans = [-1, -1]
        nums = [i for i in range(1, len(grid) * len(grid) + 1)]

        for r in grid:
            for c in r:
                if c in seen:
                    ans[0] = c
                if c in nums:
                    nums.remove(c)
                seen.add(c)
        ans[1] = nums[0]
        return ans
        