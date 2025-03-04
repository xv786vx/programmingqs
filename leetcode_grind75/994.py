# 994. Rotting Islands
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0
        directions = [[0, 1], [0, -1], [1, 0] ,[-1, 0]]

        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])
        
        while q and fresh != 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    if r + dr < 0 or r + dr >= rows or c + dc < 0 or c + dc >= cols or grid[r + dr][c + dc] != 1:
                        continue
                    grid[r + dr][c + dc] = 2
                    q.append([r + dr, c + dc])
                    fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1

