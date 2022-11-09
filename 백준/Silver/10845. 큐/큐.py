from collections import deque
import sys

queue = deque()

input = sys.stdin.readline

N = int(input())

for _ in range(N) :
  command = input().split()
  if command[0] == "push" :
    queue.append(int(command[1]))
  elif command[0] == "pop" :
    if queue :
      print(int(queue.popleft()))
    else :
      print(-1)
  elif command[0] == "size" :
    print(len(queue))
  elif command[0] == "empty" :
    if queue :
      print(0)
    else :
      print(1)
  elif command[0] == "front" :
    if queue :
      print(queue[0])
    else :
      print(-1)
  else :
    if queue :
      print(queue[-1])
    else:
      print(-1)