from queue import Queue

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        q = Queue()
        visited = [False] * n
        
        q.put(source)
        visited[source] = True
        while not q.empty():
            node = q.get()
            for to in adj[node]:
                if not visited[to]:
                    q.put(to)
                    visited[to] = True

        return visited[destination]
