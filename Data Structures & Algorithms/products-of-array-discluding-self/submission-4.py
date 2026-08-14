class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        res = []

        for num in nums:
            res.append(pre)
            pre *= num

        for i in range(len(nums)-1, -1, -1):
            res[i] *= post
            post *= nums[i]

        return res