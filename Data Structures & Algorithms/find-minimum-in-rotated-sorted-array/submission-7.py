class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]: # mid is in left split
                # search right
                l = mid + 1
            else: # mid is in right split
                r = mid

        return nums[l]

        # 3 4 5 6 1 2
        #      lm r
