class Solution:
    @cache
    def solve(self, row, col): 
        if row == 0:
            return 1

        if col == 0 or col == row:
            return 1

        return self.solve(row - 1, col - 1) + self.solve(row - 1, col)

    def getRow(self, rowIndex: int) -> List[int]:
        return [self.solve(rowIndex, colIndex) for colIndex in range(0, rowIndex + 1)]
