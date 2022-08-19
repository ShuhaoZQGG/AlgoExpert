class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        stack=[(sr, sc)]
        initialColor = image[sr][sc]
        visited = set()
        while stack:
            row, col = stack.pop()
            if image[row][col] == initialColor:
                image[row][col] = color
            visited.add((row, col))
            for dir in dirs:
                dr, dc = dir
                Row = dr + row
                Col = dc + col
                if Row >= 0 and Row < len(image) and Col >= 0 and Col < len(image[0]) and (Row, Col) not in visited and image[Row][Col] == initialColor:
                    stack.append((Row, Col))
                    visited.add((Row, Col))
        return image