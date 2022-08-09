class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        
        rows = [[] for _ in range(N)]
        cols = [[] for _ in range(N)]
        boxes = [[] for _ in range(N)]
        
        for i in range(N):
            for j in range(N):
                val = board[i][j]
                
                if val == '.':
                    continue
                
                if val in rows[i]:
                    return False
                rows[i].append(val)
            
                if val in cols[j]:
                    return False
                cols[j].append(val)
                
                idx = (i // 3) * 3 + j // 3
                if val in boxes[idx]:
                    return False
                boxes[idx].append(val)
        return True