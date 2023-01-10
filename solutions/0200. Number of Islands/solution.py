class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        directions = [[-1, 0], [+1, 0], [0, +1], [0, -1]]
        width = len(grid[0])
        height = len(grid)
        for row_idx, row in enumerate(grid):
            for col_idx, col in enumerate(row):
                if col == "0":
                    continue
                result += 1

                queue = [(row_idx, col_idx)]
                grid[row_idx][col_idx] = "0"

                while queue:
                    r, c = queue.pop(0)

                    for dr, dc in directions:
                        nr = dr + r
                        nc = dc + c

                        if 0 <= nr < height and 0 <= nc < width and grid[nr][nc] == "1":
                            grid[nr][nc] = "0"
                            queue.append((nr, nc))
        return result