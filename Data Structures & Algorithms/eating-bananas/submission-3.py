class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r




        while l <= r:
            mid = (r + l) // 2

            time = 0
            for p in piles:
                time += math.ceil(float(p) / mid)
            if time > h:
                l = mid + 1
            else:
                res = mid
                r = res - 1
        return res


