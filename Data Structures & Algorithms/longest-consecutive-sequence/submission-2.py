class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        longest = 0

        for num in nums:
            seen.add(num)
        
        for num in nums:
            if num - 1 not in seen:
                curr = num
                length = 0
                while curr in seen:
                    length += 1
                    curr += 1
                longest = max(longest, length)
            

        return longest

            