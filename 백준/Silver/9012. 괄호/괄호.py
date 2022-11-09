import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T) :
  PS = list(input().rstrip())
  sum = 0
  for i in PS :
    if i == "(" :
      sum += 1
    elif i == ")" :
      sum -= 1
    if sum < 0 :
      break
  if sum == 0 :
    print("YES")
  else :
    print("NO")