class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        freq = Counter(hand)

        for k in sorted(freq):
            while freq[k] > 0:
                for i in range(k, k + groupSize):
                    if freq[i] <= 0:
                        return False
                    freq[i] -= 1
        
        return True



