#16917. [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반
import sys
sys.stdin = open('./inputs/S_16917.txt','r')

for t in range(int(input())):
    freight_nums, truck_nums = map(int,input().split())
    freights = list(map(int,input().split()))
    trucks = list(map(int,input().split()))
    freights.sort(reverse=True)
    trucks.sort(reverse=True)

    sol = 0
    trucks_idx = 0
    for freight in freights:
        if freight <= trucks[trucks_idx]:
            sol += freight
            trucks_idx += 1
        if trucks_idx >= len(trucks):
            break
    print(f'#{t+1} {sol}')

# print(sum([5, 6, 10, 11, 11, 13, 14, 14]))
"""
10 13 14 6 11 5 11 14
5 18 17 8 9 17 18 4 1 16 15 13
14 18
14 18
13 17
11 17
11 16
10 15

"""
