class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start_pos = None
        end_pos = None
        obstacles = set()

        width = len(grid[0])
        height = len(grid)

        for row_idx, row in enumerate(grid):
            for col_idx, col in enumerate(row):
                if col == 1:
                    start_pos = (row_idx, col_idx)
                elif col == 2:
                    end_pos = (row_idx, col_idx)
                elif col == -1:
                    obstacles.add((row_idx, col_idx))
        
        start = ([start_pos], start_pos)
        queue = [start]

        directions = [(+1, 0), (-1, 0), (0, +1), (0, -1)]
        result = 0
        while queue:
            visited, (row, col) = queue.pop()
            if (row, col) == end_pos and len(visited) == width * height - len(obstacles):
                result += 1
                continue

            for drow, dcol in directions:
                nrow = drow + row
                ncol = dcol + col

                npos = (nrow, ncol)
                if nrow < 0 or nrow == height or ncol < 0 or ncol == width:
                    continue
                if npos in visited or npos in obstacles:
                    continue
                queue.append((visited + [npos], npos))
        return result