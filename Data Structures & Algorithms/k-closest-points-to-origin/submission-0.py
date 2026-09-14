class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p1, p2 in points:
            heap.append([math.sqrt((p1 - 0) ** 2 + (p2 - 0) ** 2), [p1, p2]])
        
        heapq.heapify(heap)
        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res