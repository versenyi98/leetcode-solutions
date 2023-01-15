class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        width = len(grid[0])
        height = len(grid)

        directions = [[+1, 0], [-1, 0], [0, +1], [0, -1]]

        for row_idx, row in enumerate(grid):
            for col_idx, col in enumerate(row):
                if col == 0:
                    continue

                grid[row_idx][col_idx] = 0
                queue = [(row_idx, col_idx)]
                area = 0

                while queue:
                    area += 1
                    r, c = queue.pop(0)

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < height and 0 <= nc < width and grid[nr][nc]:
                            queue.append((nr, nc))
                            grid[nr][nc] = 0
                max_area = max(area, max_area)
        return max_area