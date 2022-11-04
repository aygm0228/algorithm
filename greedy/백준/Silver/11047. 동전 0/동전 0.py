import sys

input = sys.stdin.readline

N, K = map(int, input().split())

dongjun = [] #동전의 가치 오름차순 리스트
count = 0 # 동전의 갯수

for _ in range(N) : #동전의 가치 리스트에 추가
  dongjun.append(int(input()))

dongjun.sort(reverse=True) #리스트 뒤집기

for i in dongjun :
  if i > K :
    continue

  count += K // i
  K %= i

  if K == 0 :
    break

print(count)
