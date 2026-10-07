class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        permutation = []


        def backtrack(permutation, i):
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                return
                
            for pos in range(len(permutation) + 1):
                permutation.insert(pos, nums[i])
                backtrack(permutation, i + 1)
                del permutation[pos]

        backtrack([], 0)
        return res