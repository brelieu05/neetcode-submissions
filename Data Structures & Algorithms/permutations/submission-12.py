class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = [[]]

        for num in nums:
            new_permutations = []
            for permutation in permutations:
                for pos in range(len(permutation) + 1):
                    new_permutation = permutation.copy()
                    new_permutation.insert(pos, num)
                    new_permutations.append(new_permutation)
            permutations = new_permutations
        return permutations

            
