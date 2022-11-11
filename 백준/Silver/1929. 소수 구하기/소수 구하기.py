import sys

input = sys.stdin.readline

M, N = map(int, input().split())

def sosuham(x) :
  if x == 1 : 
    return False 
  else :
    for i in range(2, int(x ** 0.5) + 1) :
      if x % i == 0 :
        return False

    return True

for j in range(M, N + 1) :
  if sosuham(j) :
    print(j)