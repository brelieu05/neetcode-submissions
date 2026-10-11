class Solution:
    def rob(self, nums: List[int]) -> int:
        first, second = 0, 0

        for i in range(len(nums)):
            current = max(first + nums[i], second)
            first = second
            second = current

        return max(first, second)