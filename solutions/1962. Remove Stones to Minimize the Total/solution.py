from heapq import heapify, heappop, heappush

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapify(piles)
        while k:
            k -= 1
            biggest = -heappop(piles)
            heappush(piles, -(biggest - biggest // 2))
        return -sum(piles)
