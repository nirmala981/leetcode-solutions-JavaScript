class Solution(object):
    def minReorder(self, n, connections):
        graph = [[] for _ in range(n)]

        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))

        visited = [False] * n

        def dfs(city):
            visited[city] = True
            count = 0

            for neighbor, cost in graph[city]:
                if not visited[neighbor]:
                    count += cost
                    count += dfs(neighbor)

            return count

        return dfs(0)
        