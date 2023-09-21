# 16890. [파이썬 S/W 문제해결 구현] 2일차 - 최소합
import sys
sys.stdin = open('./inputs/S_16890.txt','r', encoding='utf-8')
"""
3초
dfs O(V+E) : N =13*13 E=4N => 5*13*13 = 845
2,786 ms
"""

di, dj = [1,0],[0,1]
def dfs(i,j,rs):
    global sol

    if i==N-1 and j==N-1:
        if sol > rs: sol = rs
        return
    
    for move in range(2):
        ii = i+di[move]
        jj = j+dj[move]
        if 0<=ii<N and 0<=jj<N:
            rs += G[ii][jj]
            # C[ii][jj] = 1
            dfs(ii,jj,rs)
            # 백트래킹
            rs -= G[ii][jj]
            # C[ii][jj] = 0

for tc in range(int(input())):
    N = int(input())
    G = [list(map(int,input().split())) for _ in range(N)]
    # C = [[0]*N for _ in range(N)]
    sol = float('inf')
    
    dfs(0,0,G[0][0])
    print(f'#{tc+1} {sol}')
