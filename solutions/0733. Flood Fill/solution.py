class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == color:
            return image

        directions = [[-1, 0], [+1, 0], [0, +1], [0, -1]]
        width = len(image[0])
        height = len(image)

        queue = [(sr, sc)]
        image[sr][sc] = color

        while queue:
            row, col = queue.pop(0)

            for drow, dcol in directions:
                nrow = drow + row
                ncol = dcol + col

                if 0 <= nrow < height and 0 <= ncol < width and image[nrow][ncol] == original_color:
                    image[nrow][ncol] = color
                    queue.append((nrow, ncol))
        return image