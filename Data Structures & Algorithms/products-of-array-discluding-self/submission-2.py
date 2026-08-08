class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: 
        pre = 1
        post = 1
        output = []

        for i in range(len(nums)):
            output.append(pre)
            pre *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            output[i] *= post
            post *= nums[i]

        return output