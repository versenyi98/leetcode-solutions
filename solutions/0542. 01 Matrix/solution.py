class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        h, w = len(mat), len(mat[0])
        directions = [(+1, 0), (-1, 0), (0, -1), (0, +1)]

        queue = []

        for row_idx, row in enumerate(mat):
            for col_idx, col in enumerate(row):
                if col == 0:
                    queue.append((row_idx, col_idx))
                else:
                    mat[row_idx][col_idx] = -1

        while queue:
            row, col = queue.pop(0)
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if nr < 0 or nr == h or nc < 0 or nc == w or mat[nr][nc] != -1:
                    continue
                mat[nr][nc] = mat[row][col] + 1
                queue.append((nr, nc))
        return mat