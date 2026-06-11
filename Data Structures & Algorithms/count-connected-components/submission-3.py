class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = {i:[] for i in range(n)}

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        cycle = set()

        def dfs(i, prev):
            if i in cycle:
                return True
            if i in visited:
                return False

            visited.add(i)
            cycle.add(i)

            for x in adj[i]:
                if x == prev:
                    continue
                if not dfs(x, i):
                    return False
            
            return True

        counter = 0
        for i in range(n):
            cycle = set()
            if dfs(i, -1):
                counter += 1

        return counter


