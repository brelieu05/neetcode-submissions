class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        store = [intervals[0]]

        for start, end in intervals:
            self.add_interval(store, start, end)

        return store

    
    def add_interval(self, store : List[List[int]], start: int, end: int) -> None:

        # find the index whos interval starts or after start
        l, r = 0, len(store)
        while l < r:
            mid = (l + r) // 2
            if store[mid][0] < start:
                l = mid + 1
            else:
                r = mid 
                
        # [[1, 3]]
        #   lmr

        # 3 >= 4
        # [4, 10]
                # end
        #[########]
        #       [####]
                # start


        # include the left neighbor if it overlaps
        while l > 0 and store[l - 1][1] >= start: # if the end of the top of store crosses the start
            l -= 1
            start = store[l][0]
            

        #find the end of the slice to replace
        r = l
        while r < len(store) and store[r][0] <= end:
            end = max(end, store[r][1])
            r += 1


        store[l:r] = [[start, end]]

