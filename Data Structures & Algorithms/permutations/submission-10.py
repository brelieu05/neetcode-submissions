class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(permutation, i):
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                return
                
            if i >= len(nums):
                return
                
            
            for pos in range(len(permutation) + 1):
                permutation.insert(pos, nums[i])
                backtrack(permutation, i + 1)

                permutation.remove(nums[i])
                backtrack(permutation, i + 1)

            
        backtrack([], 0)
        return res