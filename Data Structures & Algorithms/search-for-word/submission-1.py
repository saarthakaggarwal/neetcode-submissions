class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        def dfs(row, col, visited, i):
            if (row, col) in visited:
                return False
            
            if word[i] != board[row][col]:
                return False

            if i == len(word) - 1:
                return True

            visited.add((row, col))
            toReturn = False

            if row > 0:
                if dfs(row - 1, col, visited, i + 1): return True
            if row < len(board) - 1:
                if dfs(row + 1, col, visited, i + 1): return True 
            if col > 0:
                if dfs(row, col - 1, visited, i + 1): return True
            if col < len(board[0]) - 1:
                if dfs(row, col + 1, visited, i + 1): return True

            visited.remove((row, col))

            return False

        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if dfs(r, c, set(), 0):
                        return True 


        return False

            





