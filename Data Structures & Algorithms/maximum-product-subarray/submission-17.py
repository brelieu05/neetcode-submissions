class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]

        first, second = nums[0], nums[0]



        for i in range(1, n):
            temp = first
            first = max(nums[i], nums[i] * first, nums[i] * second)
            second = min(nums[i], nums[i] * second, nums[i] * temp)
            res = max(res, first)
        return res
