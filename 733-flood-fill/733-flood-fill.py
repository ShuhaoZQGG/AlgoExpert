class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        stack = [(sr, sc)]
        visited = set()
        initial = image[sr][sc]
        row_length = len(image)
        col_length = len(image[0])
        while stack:
            row, col = stack.pop()
            if image[row][col] == initial:
                image[row][col] = color
            visited.add((row, col))
            for dr, dc in dirs:
                ROW = dr + row
                COL = dc + col
                if ROW in range(row_length) and COL in range(col_length) and (ROW, COL) not in visited and image[ROW][COL] == initial:
                    stack.append((ROW, COL))
                    visited.add((ROW, COL))
        return image