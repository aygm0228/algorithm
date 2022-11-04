import sys

input = sys.stdin.readline

N = int(input())

people = list(map(int,input().split())) # 각 사람들 인출 시간

people.sort()

people_sum = 0
people_time = 0

for i in people :
  people_sum += i
  people_time += people_sum

print(people_time)