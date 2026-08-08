class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        bucket = [[] for i in range(len(nums) + 1) ]

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num, count in freq.items():
            bucket[count].append(num)

        res = []
        for arr in bucket[::-1]:
            for num in arr:
                res.append(num)
                if len(res) == k:
                    return res
        return res
            
        
