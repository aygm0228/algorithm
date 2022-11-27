import sys
from collections import deque

input = sys.stdin.readline

queue = deque()

N, M = map(int, input().split()) # 사람의 수, 관계 수

# 방문 인접 행렬
state = [False for _ in range(N)]

# 관계 인접 리스트
rel = [[] for _ in range(N)]

# 관계 인접 리스트 할당하기
for _ in range(M) :
  node1, node2 = map(int, input().split())
  rel[node1].append(node2)
  rel[node1].sort()
  rel[node2].append(node1)
  rel[node2].sort()

# true, false
TF = False

# dfs 구현
def dfs(rel, v, state) :
  global count
  queue.append(v)
  state[v] = True
  if count == 4 :
    global TF
    TF = True
    return 0
  count += 1
  for j in rel[v] :
    if not state[j] :
      queue.append(j)
      state[j] = True
      dfs(rel, j, state)
      state[j] = False
      queue.pop()
  queue.pop()
  state[v] = False
  count -= 1

# 구현
for i in range(N) :
  count = 0
  if TF :
    break
  dfs(rel, i, state)

# 출력
if TF :
  print(1)
else :
  print(0)