class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        def dfs(node: int):
            visited[node] = True
            for to in adj[node]:
                if not visited[to]:
                    dfs(to)

        dfs(source)
        return visited[destination]
