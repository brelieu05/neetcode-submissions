class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqMap = {}

        for s in s1:
            freqMap[s] = freqMap.get(s, 0) + 1

        l = 0 
        for r in range(len(s2)):
            while s2[r] in freqMap and freqMap[s2[r]] == 0:
                if s2[l] in freqMap:
                    freqMap[s2[l]] += 1
                l += 1
            
            if s2[r] in freqMap:
                freqMap[s2[r]] -= 1
            else:
                while l <= r:
                    if s2[l] in freqMap:
                        freqMap[s2[l]] += 1
                    l += 1


            if sum(freqMap.values()) == 0:
                return True

        return False
