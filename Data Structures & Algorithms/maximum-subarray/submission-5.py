class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, curSum = nums[0], 0

        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSub = max(maxSub, curSum)

        return maxSub
    # nums = [-2,1,-3,4,-1,2,1,-5,4]
    # res = 