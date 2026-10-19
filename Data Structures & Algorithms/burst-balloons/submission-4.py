

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        memo = {}
        nums = [1] + nums + [1]

        def dfs(left, right):
            if left > right:
                return 0

            if (left, right) in memo:
                return memo[(left, right)]

            max_sum = float("-inf")
            for i in range(left, right + 1):
                coins = nums[left-1] * nums[i] * nums[right+1]
                max_sum = max(max_sum, dfs(left, i-1) + coins + dfs(i+1, right))

            memo[(left, right)] = max_sum
            return max_sum
        return dfs(1, len(nums) - 2)

        

            