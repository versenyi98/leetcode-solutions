from heapq import heapify, heappush, heappop
from collections import defaultdict
import math


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        routes = defaultdict(list)
        priority_queue = [(0, 0, src)]  # cost, stops, city
        visited = [(math.inf, math.inf)] * n

        for source, destination, price in flights:
            routes[source].append((destination, price))

        while priority_queue:
            cost, stops, city = heappop(priority_queue)
            if city == dst:
                return cost

            if stops == k + 1:
                continue

            if (best_steps := visited[city][1]) < stops and visited[city][0] < cost:
                continue

            if best_steps > stops:
                visited[city] = (cost, stops)

            for destination, price in routes[city]:
                heappush(priority_queue, (cost + price, stops + 1, destination))
        return -1
