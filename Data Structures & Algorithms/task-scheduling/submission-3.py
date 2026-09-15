class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = list(Counter(tasks).values())
        time = 0
        q = deque()

        heapq.heapify_max(heap)
        
        while heap or q:
            time += 1
            if heap:
                count = heapq.heappop_max(heap) - 1
                if count:
                    q.append([count, time + n])

            if q and q[0][1] == time:
                heapq.heappush_max(heap, q.popleft()[0])


        return time
