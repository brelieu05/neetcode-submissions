class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robHouses(nums):
            first, second = 0, 0

            for num in nums:
                curr = max(second, first + num)
                first = second
                second = curr
            return second
        
        return max(robHouses(nums[1:]), robHouses(nums[:-1]))

                