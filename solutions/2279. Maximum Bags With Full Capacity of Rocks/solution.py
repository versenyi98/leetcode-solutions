class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        free_space = sorted([cap - rock for cap, rock in zip(capacity, rocks)])
        idx = 0
        while idx < len(free_space) and free_space[idx] <= additionalRocks:
            additionalRocks -= free_space[idx]
            idx += 1
        return idx
