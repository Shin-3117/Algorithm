"""
N = 15
15*15 
2^15^2 : 65536
"""

import sys
import pprint
sys.stdin = open('./inputs/B_1074.txt','r', encoding='utf-8')
di = [0,0,1,1]
dj = [0,1,0,1]

N, r, c = map(int,sys.stdin.readline().split())

G = [[0]*(2**N) for _ in range(2**N)]
# N 재귀 이동

# 포문으로 N-1까지 돌리기
# 포문의 각 i 별로 
# 00 01 10 01 / 02 03 12 13
# 20 21 30 31 / 22 23 32 33

# N = 2   0 1
cnt = -1
for i in range(2):
    for j in range(2):
        for k in range(4):
            cnt += 1
            ii = i*2 +di[k]
            jj = j*2 +dj[k]
            G[ii][jj] = cnt
pprint.pprint(G)