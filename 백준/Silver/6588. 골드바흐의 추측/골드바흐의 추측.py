import sys

input = sys.stdin.readline

prime_number = [True for _ in range(1000001)]

for i in range(2, int(1000000 ** 0.5) + 1) :
  if prime_number[i] == True :
    j = 2
    while i * j <= 1000000 :
      prime_number[i * j] = False
      j += 1

def goldbach(n) :
  for k in range(3, n) :
    if k % 2 == 1 and prime_number[k] == True and prime_number[n - k] == True :
      print("%d = %d + %d"%(n, k, n - k))
      break
    if k == n - 1 :
      print('"Goldbach\'s conjecture is wrong."')

n = int(input())

while n :
  goldbach(n)
  n = int(input())