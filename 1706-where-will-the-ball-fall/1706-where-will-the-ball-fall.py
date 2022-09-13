class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        def dfs(i):
            horizontal, vertical = True, False
            stack = [(0, i)]
            while stack:
                row, col = stack.pop()
                if horizontal:
                    horizontal, vertical = not horizontal, not vertical
                    if grid[row][col] == 1:
                        col += 1
                        if col not in range(len(grid[0])) or grid[row][col] == -1 :
                            return -1
                        if row in range(len(grid)) and col in range(len(grid[0])):
                            stack.append((row, col))
                    elif grid[row][col] == -1:
                        col -= 1
                        if col not in range(len(grid[0])) or grid[row][col] == 1:
                            return -1
                        if row in range(len(grid)) and col in range(len(grid[0])):
                            stack.append((row, col))
                elif vertical:
                    horizontal, vertical = not horizontal, not vertical
                    row += 1
                    if row in range(len(grid)) and col in range(len(grid[0])):
                        stack.append((row, col))
            return col
        
        res = []
        for i in range(len(grid[0])):
            res.append(dfs(i))
        return res
            