# 200. Number of Islands
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        islands = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        def dfs(r, c):
            if grid[r][c] == "0" or (r, c) in visited:
                return
            else:
                if r - 1 >= 0:
                    dfs(r-1, c)
                if r + 1 < rows:
                    dfs(r+1, c)
                if c - 1 >= 0:
                    dfs(r, c-1)
                if c + 1 < cols:
                    dfs(r, c+1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1
        return islands