class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        visited = set()
        def bfs(grid, i, j):
            q = collections.deque([(i , j)])
            visited.add((i,j))
            while q:
                r, c = q.pop()
                dirs = [[1,0], [0,1], [0,-1], [-1, 0]]            
                for dr, dc in dirs:
                    row = r + dr
                    col = c + dc
                    if row < rows and row >= 0 and col < cols and col >= 0 and grid[row][col] == '1' and (row, col) not in visited:
                        visited.add((row, col))
                        q.append((row, col))
                 
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    bfs(grid, i, j)
                    res += 1
        return res