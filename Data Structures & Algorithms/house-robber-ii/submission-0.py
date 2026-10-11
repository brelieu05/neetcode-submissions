class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robHouse(nums):
            memo = [-1] * len(nums)
            
            def recurse(i):
                if i >= len(nums):
                    return 0

                if memo[i] != -1:
                    return memo[i]

                    
                memo[i] = max(recurse(i + 1), nums[i] + recurse(i + 2))

                return memo[i]

            return recurse(0)
        return max(robHouse(nums[1:]), robHouse(nums[:-1]))