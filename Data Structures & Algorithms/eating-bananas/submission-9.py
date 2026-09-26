class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPiles = max(piles)
        l, r = 1, maxPiles
        res = maxPiles

        while l <= r:
            mid = (l + r) // 2
            time = 0
            
            for p in piles:
                time += math.ceil(p / mid)

            if time > h:
                l = mid + 1
            else:
                r = mid - 1
                res = min(res, mid)

        return res
            

# 1 2 3 4 5 6 7 8 9 10 11
# l         m           r

# t = 6