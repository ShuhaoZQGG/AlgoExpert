class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0 for i in range(n)] for j in range(m)] 
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 or j == 0:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
        return matrix[m - 1][n - 1]