class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create set
        
        # add all the numbers to the set

        # loop through all the numbers
            # check if num - 1 in set
                # if not, start counting sequence
                    # max(longest, length)
                

        seen = set()
        
        for num in nums:
            seen.add(num)

        longest = 0
        for num in nums:
            length = 0
            if num - 1 not in seen:
                curr = num
                while curr in seen:
                    curr += 1
                    length += 1
                longest = max(longest, length)
        
        return longest
                
                