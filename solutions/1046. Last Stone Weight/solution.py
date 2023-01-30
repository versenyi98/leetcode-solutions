from heapq import heapify, heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapify(stones)
        while stones:
            first = heappop(stones)
            if not stones:
                return -first
            second = heappop(stones)
            print(first, second)
            heappush(stones, first - second)

        return 0