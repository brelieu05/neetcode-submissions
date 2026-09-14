class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapq.heapify_max(stones)
        print(heap)
        while len(heap) > 1:
            print(heap)
            x = heapq.heappop_max(heap)
            y = heapq.heappop_max(heap)
            
            if x == y:
                continue
            
            if x < y:
                heapq.heappush_max(heap, y - x)
            else:
                heapq.heappush_max(heap, x - y)

        
        return heap[0] if len(heap) > 0 else 0

        # [9, 7, 7, 6, 6]
        x = 9
        y = 7
        # [7, 6, 6, 2]

        
        