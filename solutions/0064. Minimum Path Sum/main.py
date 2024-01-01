import math
from functools import lru_cache

class Solution:
    @lru_cache(maxsize=None)
    def dp(self, row, col):
        if row == 0 and col == 0:
            return self.grid[0][0]

        if row < 0 or col < 0:
            return math.inf

        return self.grid[row][col] + min(self.dp(row - 1, col), self.dp(row, col - 1))

    def minPathSum(self, grid: List[List[int]]) -> int:
        self.grid = grid
        return self.dp(len(grid) - 1, len(grid[0]) - 1)