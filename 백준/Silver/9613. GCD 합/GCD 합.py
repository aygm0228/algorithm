import sys

input = sys.stdin.readline

t = int(input())

def GCD(A, B) :
  if B < A :
    A, B = B, A
  if B % A == 0 :
    return A
  return GCD(B % A, A)


for _ in range(t) :
  sum = 0
  l = list(map(int, input().split()))
  for i in range(1, l[0]) :
    for j in range(i + 1, l[0] + 1) :
      sum += GCD(l[i], l[j])
  print(sum)