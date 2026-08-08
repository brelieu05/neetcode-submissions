class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        longest = 0

        for num in nums:
            seen.add(num)

        for num in nums:
            curr = num
            length = 0
            
            if curr - 1 not in seen:
                while curr in seen:
                    length += 1
                    curr += 1
            longest = max(length, longest)
        
        return longest
