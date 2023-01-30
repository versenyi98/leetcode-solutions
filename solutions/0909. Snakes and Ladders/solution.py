class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        idx = 1
        direction = 1
        mapping = [(n - 1, 0)]
        first = True
        while idx != n ** 2:
            if mapping[-1][1] == 0 or mapping[-1][1] % n == n - 1:
                if first:
                    first = False
                else:
                    direction *= -1
                    mapping.append((mapping[-1][0] - 1, mapping[-1][1]))
                    idx += 1
            mapping.append((mapping[-1][0], mapping[-1][1] + direction))
            idx += 1

        queue = [(0, 0, None)]  # pos, steps

        visited = [False] * n ** 2

        while queue:
            idx, steps, parent = queue.pop(0)
            print(idx, steps, parent)
            for dice in range(1, 7):
                next_idx = idx + dice

                if next_idx == n ** 2 - 1:
                    return steps + 1
                if next_idx > n ** 2:
                    continue

                row, col = mapping[next_idx]
                if (dest := board[row][col]) != -1:
                    next_idx = dest - 1

                    if next_idx == n ** 2 - 1:
                        return steps + 1
                    if next_idx > n ** 2:
                        continue

                if visited[next_idx]:
                    continue

                visited[next_idx] = True
                queue.append((next_idx, steps + 1, (idx, dice)))
        return -1