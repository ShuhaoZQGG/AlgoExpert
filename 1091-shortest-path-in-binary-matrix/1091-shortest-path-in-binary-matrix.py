class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        max_row, max_col = len(grid) - 1, len(grid[0]) - 1
        if (grid[0][0] == 1):
            return -1
        q = deque()
        q.append((1, (0, 0)))
        visited = set()
        visited.add((0,0))
        
        dirs = [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1), (1, -1)]
        
        while q:
            distance, tmp = q.popleft()
            row, col = tmp[0], tmp[1]
            if (row, col) == (max_row, max_col):
                return distance
            
            for (i, j) in dirs:
                new_row, new_col = row + i, col + j
                if  0 <= new_row <= max_row and 0 <= new_col <= max_col and (new_row, new_col) not in visited and grid[new_row][new_col] == 0:
                    q.append((distance + 1, (new_row, new_col)))
                    visited.add((new_row, new_col))
        return -1