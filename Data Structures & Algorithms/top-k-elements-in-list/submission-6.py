class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        buckets = [[] for i in range(len(nums) + 1)]
        res = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for key, val in freq.items():
            buckets[val].append(key)

        for arr in buckets[::-1]:
            for n in arr:
                res.append(n)
        return res[:k]