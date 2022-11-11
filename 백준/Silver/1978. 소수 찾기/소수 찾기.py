import sys

input = sys.stdin.readline

N = int(input()) # 100이하의 자연수 N
count = 0
num_list = list(map(int, input().split()))

for i in num_list :
  if i == 1 :
    continue
  elif i == 2 :
    count += 1
    continue
  for j in range(2, i) :
    if i % j == 0 :
      break
    elif j == i - 1 :
      count += 1

print(count)