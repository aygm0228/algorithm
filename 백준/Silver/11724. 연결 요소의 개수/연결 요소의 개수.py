import sys

input = sys.stdin.readline

N, M = map(int, input().split()) # 정점, 간선의 개수

visited = [False for _ in range(N + 1)]

graph = [[] for _ in range(N + 1)]

for _ in range(M) :
  node1, node2 = map(int, input().split())
  graph[node1].append(node2)
  graph[node2].append(node1)
  graph[node1].sort()
  graph[node2].sort()

def dfs(graph, visited, v) :
  visited[v] = True
  for j in graph[v] :
    if not visited[j] :
      dfs(graph, visited, j)
count = 0

for i in range(1, N + 1) :
  if not visited[i] :
    dfs(graph, visited, i)
    count += 1

print(count)