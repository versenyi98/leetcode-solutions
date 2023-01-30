class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        b = board
        for row in b:
            row = list(filter(lambda x: x != '.', row))
            if len(set(row)) != len(row):
                return False

        for c in range(9):
            col = [b[r][c] for r in range(9) if b[r][c] != '.']
            if len(set(col)) != len(col):
                return False

        cells = [[] for _ in range(9)]
        for r in range(9):
            for c in range(9):
                if b[r][c] == '.':
                    continue
                cr = r // 3
                cc = c // 3

                cells[cr * 3 + cc].append(b[r][c])
        for cell in cells:
            if len(set(cell)) != len(cell):
                return False
        return True