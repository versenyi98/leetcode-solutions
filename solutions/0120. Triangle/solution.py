from functools import lru_cache


class Solution:
    @lru_cache(maxsize=None)
    def dp(self, row, col):
        if row == len(self.triangle):
            return 0

        result = self.triangle[row][col]

        down = self.dp(row + 1, col)
        right = self.dp(row + 1, col + 1)
        return result + min(down, right)

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.triangle = triangle
        return self.dp(0, 0)