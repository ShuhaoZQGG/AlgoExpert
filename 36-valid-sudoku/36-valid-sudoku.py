class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        
        rows = [[] for _ in range(N)]
        cols = [[] for _ in range(N)]
        boxes = [[] for _ in range(N)]
        
        for i in range(N):
            for j in range(N):
                if board[i][j] == '.':
                    continue
                    
                if board[i][j] in rows[i]:
                    return False
                rows[i].append(board[i][j])
                
                if board[i][j] in cols[j]:
                    return False
                cols[j].append(board[i][j])
                
                idx = (i // 3) * 3 + j // 3
                if board[i][j] in boxes[idx]:
                    return False
                boxes[idx].append(board[i][j])
        
        return True