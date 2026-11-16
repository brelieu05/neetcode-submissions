class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        store = Counter(s)
        res = []
        seen = set()

        l, r = len(s) - 1, len(s)

        while l >= 0 and l <= r:
            if s[l] not in seen:
                seen.add(s[l])
            if store[s[l]] > 0:
                store[s[l]] -= 1
            if store[s[l]] == 0:
                seen.remove(s[l])
            if len(seen) == 0:
                res.append(r - l)
                r = l
            l -= 1




        return res[::-1]
            