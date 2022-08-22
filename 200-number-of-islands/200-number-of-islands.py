class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        islands = 0
        stack = []
        visited = set()
        def dfs(i, j):
            stack.append((i, j))
            visited.add((i, j))
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while stack:
                row, col = stack.pop()
                for dr, dc in dirs:
                    Row, Col = dr + row, dc + col
                    if Row in range(len(grid)) and Col in range(len(grid[0])) and grid[Row][Col] == '1' and (Row, Col) not in visited :
                        stack.append((Row, Col))
                        visited.add((Row, Col))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    dfs(i,j)
                    islands += 1
        return islands
            