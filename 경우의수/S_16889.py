# 16889. [파이썬 S/W 문제해결 구현] 2일차 - 전자카트
import sys
sys.stdin = open('./inputs/S_16889.txt','r', encoding='utf-8')
"""
1초
순열 10! = 362,8800
"""
from itertools import permutations
for tc in range(int(input())):
    N = int(input())
    G = [list(map(int,input().split())) for _ in range(N)]

    lst = list(range(1,N))
    cases = permutations(lst,N-1)
    
    sol = float('inf')
    for case in cases:
        start = 0
        cnt = 0
        for n in case:
            cnt += G[start][n]
            start = n
        cnt += G[start][0]
        if sol > cnt:
            sol = cnt
    print(f'#{tc+1} {sol}')