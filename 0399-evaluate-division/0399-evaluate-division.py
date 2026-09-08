class Solution(object):
    def calcEquation(self, equations, values, queries):
        graph = {}

        # Build graph
        for i in range(len(equations)):
            a = equations[i][0]
            b = equations[i][1]
            value = values[i]

            if a not in graph:
                graph[a] = {}

            if b not in graph:
                graph[b] = {}

            graph[a][b] = value
            graph[b][a] = 1.0 / value

        # DFS
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0

            if start == end:
                return 1.0

            visited.add(start)

            for neighbor, value in graph[start].items():
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)

                    if result != -1.0:
                        return value * result

            return -1.0

        answer = []

        for start, end in queries:
            answer.append(dfs(start, end, set()))

        return answer
        