class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        curr = len(nums)
        for i in range(len(nums)):
            curr ^= i ^ nums[i]
        return curr

