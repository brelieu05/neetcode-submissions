class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first, second = 0, 0
        for i in range(len(cost)):
            current = min(first, second) + cost[i]
            first = second
            second = current
        
        return min(first, second)
    

        