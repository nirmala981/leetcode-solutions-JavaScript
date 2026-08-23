from collections import Counter

class Solution:
    def equalPairs(self, grid):
        rows = Counter(tuple(row) for row in grid)

        ans = 0
        n = len(grid)

        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))
            ans += rows[col]

        return ans
        