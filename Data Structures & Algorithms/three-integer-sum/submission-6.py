class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0

        # -1, 0, 1, 2, -1, -4
        # -4, -1, -1, 0, 1, 2
        #          i  l  r
        while i < len(nums):
            l, r = i + 1, len(nums) - 1
            while l < r:
                if (nums[i] + nums[l] + nums[r]) == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
            i += 1
            while i < len(nums) and nums[i - 1] == nums[i]:
                i += 1
        return res
