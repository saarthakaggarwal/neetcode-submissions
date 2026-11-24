class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        



        def bfs(row, col):
            visited = set()
            q = deque([(row, col)])
            visited.add((row, col))



            while q:
                r, c = q.popleft()
                grid[r][c] = "0"

                if r > 0 and grid[r-1][c] == "1" and (r - 1, c) not in visited:
                    q.append((r-1, c))
                    visited.add((r-1, c))
                if r < len(grid) - 1 and grid[r + 1][c] == "1" and (r + 1, c) not in visited:
                    q.append((r+1, c))
                    visited.add((r+1, c))
                if c > 0 and grid[r][c-1] == "1" and (r, c - 1) not in visited:
                    q.append((r, c-1))
                    visited.add((r, c-1))
                if c < len(grid[0]) - 1 and grid[r][c+1] == "1" and (r, c + 1) not in visited:
                    q.append((r, c+1))
                    visited.add((r, c+1))

        counter = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    bfs(r, c)
                    counter += 1

        return counter