import math


class Solution:
    def dp(self, idx):
        if idx in [0, 1]:
            return self.cost[idx]

        if self.memo[idx] != math.inf:
            return self.memo[idx]

        self.memo[idx] = 0 if idx == len(self.cost) else self.cost[idx]
        self.memo[idx] += min(self.dp(idx - 1), self.dp(idx - 2))
        return self.memo[idx]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.memo = [math.inf] * (len(cost) + 1)
        self.cost = cost
        return self.dp(len(cost))