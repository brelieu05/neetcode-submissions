class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = list(freq.values())
        heapq.heapify_max(heap)

        time = 0
        q = deque()

        while heap or q:
            time += 1

            # Tasks whose cooldown has ended
            if q and q[0][1] <= time:
                heapq.heappush_max(heap, q.popleft()[0])

            # Execute task
            if heap:
                freq = heapq.heappop_max(heap) - 1

                if freq:
                    q.append([freq, time + n + 1])

        return time