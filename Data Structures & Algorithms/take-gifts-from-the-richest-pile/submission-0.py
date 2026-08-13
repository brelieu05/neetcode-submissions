class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        while k > 0:
            gifts[gifts.index(max(gifts))] = int(sqrt(gifts[gifts.index(max(gifts))]))
            k -= 1

        return sum(gifts)
            