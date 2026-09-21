class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        result = []
        directions = [[1,0], [0,1], [-1,0], [0,-1]]



        def bfs(r, c):
            visited = set()
            queue = deque()
            queue.append([r,c])
            visited.add((r,c))

            pacific, atlantic = False, False

            while queue:
                x, y = queue.popleft()
                if x == 0 or y == 0:
                    pacific = True
                if y == COLS - 1 or x == ROWS - 1:
                    atlantic = True

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx >= 0 and ny >= 0 and nx < ROWS and ny < COLS and (nx, ny) not in visited and heights[x][y] >= heights[nx][ny]:
                        visited.add((nx, ny))
                        queue.append([nx, ny])


            return (pacific and atlantic)



        for i in range(ROWS):
            for j in range(COLS):
                if bfs(i, j):
                    result.append([i,j])


        return result