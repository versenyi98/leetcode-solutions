class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
    
        rows = [""] * numRows

        current_row = 0
        direction = 1
        
        idx = 0

        while idx != len(s):
            rows[current_row] += s[idx]
            idx += 1
            current_row += direction

            if current_row == 0 or current_row == numRows - 1:
                direction *= -1
        return "".join(rows)