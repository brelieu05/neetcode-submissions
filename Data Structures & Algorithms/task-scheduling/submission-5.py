class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = list(Counter(tasks).values())
        heapq.heapify_max(freq)

        q = deque()
        time = 0

        while freq or q:
            time += 1

            if q and q[0][1] == time:
                heapq.heappush_max(freq, q.popleft()[0])

            if freq:
                count = heapq.heappop_max(freq) - 1
                if count:
                    q.append((count, time + n + 1))
            

        return time
                