class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m, n = len(matrix), len(matrix[0])
        i, j = 0, -1
        direction = 1
        while len(res) != len(matrix) * len(matrix[0]):
            for _ in range(n):
                j += direction
                res.append(matrix[i][j])
            m -= 1
            for _ in range(m):
                i += direction
                res.append(matrix[i][j])
            n -= 1
            direction *= -1
        return res