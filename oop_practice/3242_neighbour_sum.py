class NeighborSum:

    def __init__(self, grid: list[list[int]]):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        

    def adjacentSum(self, value: int) -> int:
        summation = 0
        i, j = self.find_pos(value)
        if i == -1 and j == -1:
            return summation

        # sum up:
        if i - 1 < 0:
            pass
        else:    
            summation += self.grid[i-1][j]

        # sum down
        if i + 1 >= self.rows:
            pass
        else:    
            summation += self.grid[i+1][j]

        # sum left
        if j - 1 < 0:
            pass
        else:    
            summation += self.grid[i][j-1]

        # sum right
        if j + 1 >= self.cols:
            pass
        else:    
            summation += self.grid[i][j+1]
        return summation
        

    def diagonalSum(self, value: int) -> int:
        summation = 0
        i, j = self.find_pos(value)

        # sum top left:
        if i - 1 < 0 or j - 1 < 0:
            pass
        else:    
            summation += self.grid[i-1][j-1]

        # sum bottom left:
        if i + 1 >= self.rows or j - 1 < 0:
            pass
        else:    
            summation += self.grid[i+1][j-1]

        # sum top right
        if i - 1 < 0 or j + 1 >= self.cols:
            pass
        else:    
            summation += self.grid[i-1][j+1]

        # sum bottom right
        if i + 1 >= self.rows or j + 1 >= self.cols:
            pass
        else:    
            summation += self.grid[i+1][j+1]
        return summation



    # def dfs_matrix(self, node):
    #     visited = set()
    #     rows, cols = len(self.grid), len(self.grid[0])
    #     def dfs(i, j):
    #         if i < 0 or i >= rows or j < 0 or j >= cols:
    #             return False

    #         visited.add((i, j))

    #         if self.grid[i][j] == node:
    #             return (i, j)
            
    #         if dfs(i - 1, j):
    #             return (i, j)
    #         if dfs(i + 1, j):
    #             return (i, j)
    #         if dfs(i, j - 1):
    #             return (i, j)
    #         if dfs(i, j + 1):
    #             return (i, j)
            
    #         return False
    #     return dfs(0, 0)
    def find_pos(self, value):
        for i in range(0, self.rows):
            for k in range(0, self.cols):
                if self.grid[i][k] == value:
                    return (i, k)
        return (-1, -1)
        


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)