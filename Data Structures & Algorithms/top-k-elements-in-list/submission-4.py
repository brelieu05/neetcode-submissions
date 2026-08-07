class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for key, val in count.items():
            freq[val].append(key)

        res = []
        for arr in freq[::-1]:
            for n in arr:
                res.append(n)

        return res[:k]
