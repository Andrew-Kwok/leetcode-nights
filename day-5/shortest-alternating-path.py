class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        adj = [[[] for _ in range(n)] for _ in range(2)]
        for e in redEdges:
            adj[0][e[0]].append(e[1])
        for e in blueEdges:
            adj[1][e[0]].append(e[1])

        q = Queue()
        distance = [[-1]*n, [-1]*n]
        
        distance[0][0] = 0
        distance[1][0] = 0
        q.put((0, 0))
        q.put((0, 1))

        while not q.empty():
            node, prev = q.get()

            color = 1 - prev
            for to in adj[color][node]:
                if distance[color][to] == -1:
                    distance[color][to] = distance[prev][node] + 1
                    q.put((to, color))

        ans = [-1] * n
        for i in range(n):
            candidate = {distance[color][i] for color in range(2) if distance[color][i] != -1 }
            if len(candidate) > 0:
                ans[i] = min(candidate)

        return ans

