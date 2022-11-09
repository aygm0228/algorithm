import sys

input = sys.stdin.readline

# 유클리드 호제법과 재귀를 이용하여 최소공배수 함수 만들기
def GCD(a, b) :
  if a % b == 0 :
    return b

  return GCD(b, a % b)

def LCM(a, b) :
  return (a * b) // GCD(a, b)

A, B = map(int,input().split())

if B > A :
  A, B = B, A

print(GCD(A, B))
print(LCM(A, B))