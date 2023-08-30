# 1247. [S/W 문제해결 응용] 3일차 - 최적 경로
import sys
sys.stdin = open('./inputs/S_1247.txt','r', encoding='utf-8')
"""
30초
고객의 수 N은 2≤N≤10 이다.
좌표의 값은 0이상 100 이하

순열 10! : 362,8800
tc =10  3628,8000
for 10 3,6288,0000
"""
from itertools import permutations

for tc in range(int(input())):
    N = int(input())
    data = list(map(int,input().split()))
    # data[0],data[1]은 회사 좌표
    # data[2],data[3]은 집 좌표
    # 나머지는 고객의 좌표
    company_i = data.pop(0)
    company_j = data.pop(0)
    home_i = data.pop(0)
    home_j = data.pop(0)
    # client = []
    # for i in range(N):
    #     client.append([data[i*2],data[i*2+1]])

    # 회사 -> 고객 -> 고객 ... -> 집
    # 순열으로 경우의 수를 구하고 각각의 경우의 수 결과 값 비교
    P = permutations(list(range(N)))
    sol = float('inf')
    # 중복 계산을 방지하기 위한 그래프 (고객 간의 거리)
    G = [[0]*(N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            G[i][j] = abs(data[i*2] - data[j*2]) + abs(data[i*2+1] - data[j*2+1])
    # print(data)
    # print(G)
    for lst in P:
        cnt = 0
        # 회사에서 고객 거리
        cnt += abs(company_i - data[lst[0]*2]) + abs(company_j - data[lst[0]*2+1])
        # 고객 간의 거리
        for idx in range(N-1):
            cnt += G[lst[idx]][lst[idx+1]]
        # 고객 - 집 거리
        cnt += abs(home_i - data[lst[-1]*2]) + abs(home_j - data[lst[-1]*2+1])
        if sol > cnt : sol = cnt

    print(f'#{tc+1} {sol}')
