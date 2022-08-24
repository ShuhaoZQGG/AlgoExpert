class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def findPaths(m, n):
            if (m == 1 and (n == 1 or n == 2)) or (n == 1 and (m == 1 or m == 2)):
                return 1
            else:
                if m == 1:
                    return findPaths(m, n - 1)
                elif n == 1:
                    return findPaths(m - 1, n)
                else:
                    return findPaths(m, n - 1) + findPaths(m - 1, n)
        return findPaths(m, n)