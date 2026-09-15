class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = list(freq.values())
        heapq.heapify_max(heap)

        q = deque()
        time = 0

        while heap or q:
            time += 1

            if q and q[0][1] <= time:
                heapq.heappush_max(heap, q.popleft()[0])
            
            if heap:
                count = heapq.heappop_max(heap) - 1

                if count:
                    q.append([count, time + n + 1])

        return time
