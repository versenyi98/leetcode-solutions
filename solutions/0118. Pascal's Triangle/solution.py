class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]

        for i in range(numRows - 1):
            row = [1] + [rows[-1][i] + rows[-1][i + 1] for i in range(len(rows[-1]) - 1)] + [1]
            rows.append(row)
        return rows