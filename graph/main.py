import collections

class Graph:
    def __init__(self, matrix: list[list[int]]):
        self.graph = matrix
        self.size = len(matrix)
    
    def dfs(self, vertex: int):
        if vertex > self.size or vertex <= 0:
            return
        v = vertex - 1
        visited = [0] * self.size
        visited[v] = 1
        q = collections.deque([v])
        while len(q):
            u = q.pop()
            print(u + 1, end = "")
            for i in range(self.size):
                if self.graph[u][i] == 1 and visited[i] == 0:
                    q.append(i)
                    visited[i] = 1


    def bfs(self, vertex: int):
        if vertex > self.size or vertex <= 0:
            return
        v = vertex - 1
        visited = [0] * self.size
        visited[v] = 1
        q = collections.deque([v])
        while len(q):
            u = q.popleft()
            print(u + 1, end="")
            for i in range(self.size):
                if self.graph[u][i] == 1 and visited[i] == 0:
                    q.append(i)
                    visited[i] = 1


if __name__ == "__main__":
    matrix = [
        [0,1,1,1,0,0,0],
        [1,0,1,0,0,0,0],
        [1,1,0,1,1,0,0],
        [1,0,1,0,1,0,0],
        [0,0,1,1,0,1,1],
        [0,0,0,0,1,0,0],
        [0,0,0,0,1,0,0],
    ]
    
    graph = Graph(matrix)
    graph.dfs(1)