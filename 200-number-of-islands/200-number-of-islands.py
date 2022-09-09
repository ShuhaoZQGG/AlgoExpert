class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set((0,0))
        ans = 0
                            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == "1":
                    ans += 1
                    stack = [(i,j)]
                    while stack:
                            row, col = stack.pop()
                            for dr, dc in dirs:
                                ROW = dr + row
                                COL = dc + col
                                if ROW in range(len(grid)) and COL in range(len(grid[0])) and grid[ROW][COL] == "1" and (ROW, COL) not in visited:
                                    stack.append((ROW, COL))
                                    visited.add((ROW, COL))                    
                    
                
        return ans
                    
                
            