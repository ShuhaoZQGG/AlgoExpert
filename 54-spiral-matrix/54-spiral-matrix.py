class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        minRow = 0
        maxRow = len(matrix) - 1
        minCol = 0
        maxCol = len(matrix[0]) - 1
        while len(res) < len(matrix) * len(matrix[0]):
            for i in range(minCol, maxCol + 1, 1):
                res.append(matrix[minRow][i])
            minRow += 1
            
            if len(res) == len(matrix) * len(matrix[0]):
                break
                
            for i in range(minRow, maxRow + 1, 1):
                res.append(matrix[i][maxCol])
            maxCol -= 1
            
            if len(res) == len(matrix) * len(matrix[0]):
                break
                
            for i in range(maxCol, minCol - 1, -1):
                res.append(matrix[maxRow][i])
            maxRow -= 1
    
            if len(res) == len(matrix) * len(matrix[0]):
                break
                
            for i in range(maxRow, minRow - 1, -1):
                res.append(matrix[i][minCol])
            minCol += 1
            
            if len(res) == len(matrix) * len(matrix[0]):
                break

        return res