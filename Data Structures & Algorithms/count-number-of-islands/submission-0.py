class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]



        def bfs(r, c):
            queue = deque([(r,c)])
            visited.add((r, c))
            
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    
                    if ((nx, ny) not in visited) and nx >= 0 and ny >= 0 and nx < rows and ny < cols and grid[nx][ny] == "1":
                        queue.append((nx, ny))
                        visited.add((nx, ny))
                    


        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1

        return islands