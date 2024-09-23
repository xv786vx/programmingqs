# 733. Flood Fill

#dfs recursion (my way) with visited matrix array (more storage)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]
        image[sr][sc] = color
        visited = [[False for _ in range(len(image[0]))] for _ in range(len(image))]
        visited[sr][sc] = True

        def fill(image, y, x, start_color, color):
            # up
            if y > 0 and image[y-1][x] == start_color and not visited[y-1][x]:
                image[y-1][x] = color
                visited[y-1][x] = True
                fill(image, y-1, x, start_color, color)

            # down
            if y + 1 < len(image) and image[y+1][x] == start_color and not visited[y+1][x]:
                image[y+1][x] = color
                visited[y+1][x] = True
                fill(image, y+1, x, start_color, color)

            # left
            if x > 0 and image[y][x-1] == start_color and not visited[y][x-1]:
                image[y][x-1] = color
                visited[y][x-1] = True
                fill(image, y, x-1, start_color, color)

            # right
            if x + 1 < len(image[0]) and image[y][x+1] == start_color and not visited[y][x+1]:
                image[y][x+1] = color
                visited[y][x+1] = True                
                fill(image, y, x+1, start_color, color)

        fill(image, sr, sc, start_color, color)

        return image
    


#dfs recursion (my way) (less storage)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]
        image[sr][sc] = color

        def fill(image, y, x, start_color, color):
            # up
            if y > 0 and image[y-1][x] == start_color and image[y-1][x] != color:
                image[y-1][x] = color
                fill(image, y-1, x, start_color, color)

            # down
            if y + 1 < len(image) and image[y+1][x] == start_color and image[y+1][x] != color:
                image[y+1][x] = color
                fill(image, y+1, x, start_color, color)

            # left
            if x > 0 and image[y][x-1] == start_color and image[y][x-1] != color:
                image[y][x-1] = color
                fill(image, y, x-1, start_color, color)

            # right
            if x + 1 < len(image[0]) and image[y][x+1] == start_color and image[y][x+1] != color:
                image[y][x+1] = color
                fill(image, y, x+1, start_color, color)

        fill(image, sr, sc, start_color, color)

        return image

    
#dfs recursion (lc recommended)
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        old_color = image[sr][sc]
        if old_color == color:
            return image
        def dfs(r, c):
            if image[r][c] == old_color:
                image[r][c] = color
                if r >= 1:
                    dfs(r - 1, c)
                if r + 1 < len(image):
                    dfs(r + 1 ,c)
                if c >= 1:
                    dfs(r, c - 1)
                if c + 1 < len(image[0]):
                    dfs(r, c + 1)
        dfs(sr, sc)
        return image



#oli's solution
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]
        image[sr][sc] = color
        queue = [(sr, sc)]

        while queue:
            y, x = queue.pop(-1)

            if y > 0 and not image[y-1][x] == color and image[y-1][x] == start_color:
                queue.append((y-1, x))
                image[y-1][x] = color
            
            if y + 1 < len(image) and not image[y+1][x] == color and image[y+1][x] == start_color:
                queue.append((y+1, x))
                image[y+1][x] = color
            
            if x > 0 and not image[y][x-1] == color and image[y][x-1] == start_color:
                queue.append((y, x-1))
                image[y][x-1] = color
            
            if x + 1 < len(image[0]) and not image[y][x+1] == color and image[y][x+1] == start_color:
                queue.append((y, x+1))
                image[y][x+1] = color
        
        return image






        






