class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for i in range(n)] for j in range(n)]
        counter = 1
        rowBegin = 0
        rowEnd = n - 1
        columnBegin = 0
        columnEnd = n - 1
        while (rowBegin <= rowEnd and columnBegin <= columnEnd):
            for i in range(columnBegin, columnEnd + 1):
                matrix[rowBegin][i] = counter
                counter += 1
            rowBegin += 1
            
            for i in range(rowBegin, rowEnd + 1):
                matrix[i][columnEnd] = counter
                counter += 1
            columnEnd -= 1

            
            for i in range(columnEnd, columnBegin - 1, -1):
                matrix[rowEnd][i] = counter
                counter += 1
            rowEnd -= 1
            
            for i in range(rowEnd, rowBegin - 1, -1):
                matrix[i][columnBegin] = counter
                counter += 1
            columnBegin += 1
        return matrix