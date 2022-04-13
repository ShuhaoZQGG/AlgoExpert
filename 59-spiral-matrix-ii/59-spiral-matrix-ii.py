class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for i in range(n)] for j in range(n)]
        counter = 1
        for layer in range((n+1)//2):
            for ptr in range(layer, n-layer):
                matrix[layer][ptr] = counter
                counter += 1

            
            for ptr in range(layer + 1, n-layer):
                matrix[ptr][n-layer-1] = counter
                counter += 1
            
            for ptr in range(layer + 1, n-layer):
                matrix[n - layer - 1][n - ptr - 1] = counter
                counter += 1
                
            for ptr in range(layer + 1, n-layer-1):
                matrix[n - ptr - 1][layer] = counter
                counter += 1
        return matrix