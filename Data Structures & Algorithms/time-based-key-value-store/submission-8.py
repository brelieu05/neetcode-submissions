class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.cache[key]) - 1

        res = []
        while l <= r:
            mid = (l + r) // 2
            curr = self.cache[key][mid]
            if curr[0] > timestamp:
                r = mid - 1
            else:
                res = curr
                l = mid + 1

        return res[1] if res and res[0] <= timestamp else ""
        