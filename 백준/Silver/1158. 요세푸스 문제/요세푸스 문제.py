from collections import deque
import sys

queue = deque()
yoseputh = []

input = sys.stdin.readline

N, K = map(int,input().split())

for i in range(1, N + 1) :
  queue.append(i)
  
while queue :
  for _ in range(K - 1) :
    queue.append(queue.popleft())
  
  yoseputh.append(queue.popleft())

yoseputh = list(map(str, yoseputh))

print("<", ", ".join(yoseputh), ">", sep="")