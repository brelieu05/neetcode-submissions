class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)

        dp = []
        dp.append(cost[0])
        dp.append(cost[1])

        for i in range(2, len(cost)):
            dp.append(min(dp[i-1], dp[i-2]) + cost[i])
        
        print(dp)
        return min(dp[-2], dp[-1])
    

        