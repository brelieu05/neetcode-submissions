class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        res = float('-inf')

        for num in nums:
            if total < 0:
                total = 0

            total += num
            res = max(res, total)

        return res