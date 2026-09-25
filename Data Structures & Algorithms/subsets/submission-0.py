class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(local, i):
            if i >= len(nums):   
                res.append(local.copy())
                return

            #include
            local.append(nums[i])
            dfs(local, i + 1)

            # exclude
            local.pop()
            dfs(local, i + 1)


        dfs([], 0)
        return res