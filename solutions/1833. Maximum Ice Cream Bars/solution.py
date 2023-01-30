class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        idx = 0

        while idx < len(costs) and coins - costs[idx] >= 0:
            coins -= costs[idx]
            idx += 1
        return idx