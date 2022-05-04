class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        curr = 0
        res = 0
        visited = set()
        def bfs(grid, i, j):
            nonlocal res
            nonlocal curr
            curr = 0
            q = collections.deque([(i , j)])
            visited.add((i,j))
            while q:
                curr += 1
                r, c = q.pop()
                dirs = [[1,0], [0,1], [0,-1], [-1, 0]]            
                for dr, dc in dirs:
                    row = r + dr
                    col = c + dc
                    if row < rows and row >= 0 and col < cols and col >= 0 and grid[row][col] == 1 and (row, col) not in visited:
                        visited.add((row, col))
                        q.append((row, col))
                    res = max(curr, res)

                 
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    curr = 0
                    bfs(grid, i, j)
        return res