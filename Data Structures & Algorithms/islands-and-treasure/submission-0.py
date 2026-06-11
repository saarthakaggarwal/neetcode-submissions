class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0,1], [1,0], [-1, 0], [0, -1]]
        visit = set()
        q = deque()

        def bfs(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] == -1:
                return
            visit.add((r,c))
            q.append([r,c])

        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append([i,j])
                    visit.add((i,j))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for d in directions:
                    nr, nc = d[0] + r, d[1] + c
                    bfs(nr, nc)

            dist += 1


            