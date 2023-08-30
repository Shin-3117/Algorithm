# 16890. [파이썬 S/W 문제해결 구현] 2일차 - 최소합
import sys
sys.stdin = open('./inputs/S_16890.txt','r', encoding='utf-8')
"""
3초
bfs O(V+E) : N =13*13 E=4N => 5*13*13 = 845
이전 값을 합하며 경로합의 C 만들기
"""
from collections import deque
di, dj = [1,0],[0,1]
def bfs(i,j):
    q = deque()
    q.append((i,j))
    C[i][j] = G[i][j]
    while q:
        i0,j0 = q.popleft()
        for move in range(2):
            ii = i0+di[move]
            jj = j0+dj[move]
            if 0<=ii<N and 0<=jj<N:
                # 방문한적이 없다면 합한 값 갱신
                if C[ii][jj] == 0 or C[ii][jj] > G[ii][jj] + C[i0][j0]:
                    C[ii][jj] = G[ii][jj] + C[i0][j0]
                    q.append((ii,jj))

for tc in range(int(input())):
    N = int(input())
    G = [list(map(int,input().split())) for _ in range(N)]
    C = [[0]*N for _ in range(N)]
    
    bfs(0,0)
    sol = C[N-1][N-1]
    print(f'#{tc+1} {sol}')
"""
#1 15
#2 18
#3 33
"""