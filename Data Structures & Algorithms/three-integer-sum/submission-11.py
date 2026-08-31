class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        # [-2, 0, 0, 2, 2]
        #  i      l  r

        i = 0
        while i < len(nums):
            while i > 0 and i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
            i += 1
        
        return res

            



                
