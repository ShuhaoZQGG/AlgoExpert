class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        islands = 0
        queue = collections.deque()
        visited = set()
        def dfs(i, j):
            queue.append((i, j))
            visited.add((i, j))
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while queue:
                row, col = queue.popleft()
                for dr, dc in dirs:
                    Row, Col = dr + row, dc + col
                    if Row in range(len(grid)) and Col in range(len(grid[0])) and grid[Row][Col] == '1' and (Row, Col) not in visited :
                        queue.append((Row, Col))
                        visited.add((Row, Col))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    dfs(i,j)
                    islands += 1
        return islands
            