class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        arr = self.store[key]
        l, r = 0, len(arr) - 1

        res = ""

        while l <= r:
            mid = (r + l) // 2
            if arr[mid][0] > timestamp:
                r = mid - 1
            else:
                res = arr[mid][1]
                l = mid + 1

        return res
        

#  one : [10, 20, 30], test: [15, 25]
        #   l.  m.   r     
# lmr