import sys
from collections import deque

input = sys.stdin.readline

queue = deque()

def dfs(V) :
  visited_dfs[V] = 1
  print(V, end=" ")
  for i in range(1, N + 1) :
    if visited_dfs[i] == 0 and graph[V][i] == 1 :
      dfs(i)

def bfs(V) :
  visited_bfs[V] = 1
  queue.append(V)
  # 큐 안에 모든 데이터가 없어 질 때까지 반복
  while queue :
    v = queue.popleft()
    print(v, end=" ")
    for j in range(1, N + 1) :
      if graph[v][j] == 1 and visited_bfs[j] == 0 :
        queue.append(j)
        visited_bfs[j] = 1


N, M, V = map(int, input().split())

# 인접 영행렬으로 전부 초기화
graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

# 입력받은 값 영행렬에 삽입
for _ in range(M) :
  node1, node2 = map(int, input().split())
  graph[node1][node2] = graph[node2][node1] = 1

# 방문할 값 리스트 만들기
visited_dfs = [0 for _ in range(N + 1)]
visited_bfs = [0 for _ in range(N + 1)]

dfs(V)
print()
bfs(V)