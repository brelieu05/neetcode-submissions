class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        length = 0


        # zyxxyz
        #    l r
        seen = {} # char seen : index
        while r < len(s) and l <= r:
            if s[r] not in seen:
                seen[s[r]] = r
                length = max(length, r - l + 1)
            else:
                index = seen[s[r]]
                while l <= index:
                    seen.pop(s[l])
                    l += 1
                seen[s[r]] = r
            r += 1

        return length
                    

                

                

            