class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        store = []

        for start, end in intervals:
            self.add_interval(store, start, end)

        return store

    
    def add_interval(self, store : List[List[int]], start: int, end: int) -> None:
        # find the insertion point using binary search
        l, r = 0, len(store) - 1
        while l <= r:
            mid = (l + r) // 2
            if store[mid][0] < start:
                l = mid + 1
            else:
                r = mid - 1

        # check left to see if it needs to be merged
        if l > 0 and store[l - 1][1] >= start:
            l -= 1
            start = min(start, store[l][0])

        # check right REPEATEDLY to see if it needs to be merged
        r = l
        while r < len(store) and store[r][0] <= end:
            end = max(end, store[r][1])
            r += 1
            
        store[l:r] = [[start, end]]

        