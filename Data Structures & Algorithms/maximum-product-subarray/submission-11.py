from functools import lru_cache

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # n = len(nums)
        # dp = [[0, 0] for _ in range(n)] # max, min
        
        # dp[0][0], dp[0][1] = nums[0], nums[0]
        # res = nums[0]

        # for i in range(1, n):
        #     valMax = nums[i] * dp[i-1][0]
        #     valMin = nums[i] * dp[i-1][1]

        #     dp[i][0] = max(nums[i], valMax, valMin)
        #     dp[i][1] = min(nums[i], valMax, valMin)
        #     res = max(res, dp[i][0])
        # return res
        n = len(nums)
        res = nums[0]

        @lru_cache
        def dfs(i):
            if i == 0:
                return (nums[0], nums[0])

            prevMin, prevMax = dfs(i - 1)

            currMin, currMax = prevMin * nums[i], prevMax * nums[i]

            return (min(currMin, currMax, nums[i]), max(currMin, currMax, nums[i]))


        for i in range(n):
            res = max(res, dfs(i)[1])
        return res
            


            




