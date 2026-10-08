class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = [[]]

        for num in nums:
            temp = []
            for permutation in permutations:
                for pos in range(len(permutation) + 1):
                    curr_permutation = permutation.copy()
                    curr_permutation.insert(pos, num)
                    temp.append(curr_permutation)
            permutations = temp
        return permutations

            
