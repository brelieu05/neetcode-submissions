class Solution:
    def rob(self, nums: List[int]) -> int:
        # if len(nums) <= 2:
        #     return max(nums)

        # dp = [0 for _ in range(len(nums))]
        # dp[1] = max(nums[0], nums[1])

        first, second = 0, 0

        for i in range(len(nums)):
            current = nums[i] + first
            first = second
            second = max(first, current)
            
        return max(first, second)
            
        