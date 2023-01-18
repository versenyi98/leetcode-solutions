class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
        fresh_oranges = set()
        queue = []

        for row_idx, row in enumerate(grid):
            for col_idx, col in enumerate(row):
                if col == 2:
                    queue.append(((row_idx, col_idx), 0))
                elif col == 1:
                    fresh_oranges.add((row_idx, col_idx))

        minute = 0

        while queue:
            (row, col), depth = queue.pop(0)
            minute = depth
            for row_dir, col_dir in directions:
                new_row = row + row_dir
                new_col = col + col_dir

                if (new_pos := (new_row, new_col)) in fresh_oranges:
                    queue.append((new_pos, depth + 1))
                    fresh_oranges.discard(new_pos)
        if fresh_oranges:
            return -1
        return minute