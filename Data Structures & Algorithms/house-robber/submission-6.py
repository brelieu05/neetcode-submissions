class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def recurse(i):
            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]

            # choice 1
            choice1 = nums[i] + recurse(i + 2)

            # choice 2
            choice2 = recurse(i + 1)

            memo[i] = max(choice1, choice2)
            return max(choice1, choice2)

        return recurse(0)