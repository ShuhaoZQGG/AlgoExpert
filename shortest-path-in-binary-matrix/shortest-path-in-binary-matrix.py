class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        max_row, max_col = len(grid) - 1, len(grid[0]) - 1
        
        if (grid[0][0] == 1):
            return -1
        
        start_point = (1, (0,0))
        
        queue = deque()
        queue.append(start_point)
        visited = set()
        visited.add(start_point[1])
        
        dirs = [(1,0),(0,1),(1,-1),(-1,1),(0,-1),(-1,0),(1,1),(-1,-1)]
        
        while queue:
            distance, node = queue.popleft()
            row, col = node[0], node[1]
            if (row, col) == (max_row, max_col):
                return distance
            for i, j in dirs:
                new_row = row + i
                new_col = col + j
                if (0<=new_row<=max_row and 0<=new_col<=max_col and grid[new_row][new_col] == 0 and (new_row, new_col) not in visited):
                    queue.append((distance+1, (new_row, new_col)))
                    visited.add((new_row, new_col))
        return -1
        