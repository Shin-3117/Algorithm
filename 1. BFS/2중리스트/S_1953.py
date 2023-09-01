# 1953. [모의 SW 역량테스트] 탈주범 검거
import sys
sys.stdin = open('./inputs2/S_1953.txt','r')
"""
50개의 테스트 케이스 15초
(5 ≤ N, M ≤ 50)
(1 ≤ L ≤ 20)

BFS로 
"""
from collections import deque
directions = [(1,0),(-1,0),(0,1),(0,-1)]

movePipe = {
    0 : [],
    1 : [(1,0),(-1,0),(0,1),(0,-1)],
    2 : [(1,0),(-1,0)],
    3 : [(0,1),(0,-1)],
    4 : [(-1,0),(0,1)],
    5 : [(1,0),(0,1)],
    6 : [(1,0),(0,-1)],
    7 : [(-1,0),(0,-1)]
}
def canMove(EndPipe, di, dj):
    if EndPipe == 0: return False
    # -> 좌에서 우로
    if di == 0 and dj ==1:
        if EndPipe == 1: return True
        elif EndPipe == 2: return False
        elif EndPipe == 3: return True
        elif EndPipe == 4: return False
        elif EndPipe == 5: return False
        elif EndPipe == 6: return True
        elif EndPipe == 7: return True
    # <- 우에서 좌로
    elif di == 0 and dj == -1:
        if EndPipe == 1: return True
        elif EndPipe == 2: return False
        elif EndPipe == 3: return True
        elif EndPipe == 4: return True
        elif EndPipe == 5: return True
        elif EndPipe == 6: return False
        elif EndPipe == 7: return False
    # 아래에서 위로
    elif di == -1 and dj == 0:
        if EndPipe == 1: return True
        elif EndPipe == 2: return True
        elif EndPipe == 3: return False
        elif EndPipe == 4: return False
        elif EndPipe == 5: return True
        elif EndPipe == 6: return True
        elif EndPipe == 7: return False
    # 위에서 아래로
    elif di == 1 and dj == 0:
        if EndPipe == 1: return True
        elif EndPipe == 2: return True
        elif EndPipe == 3: return False
        elif EndPipe == 4: return True
        elif EndPipe == 5: return False
        elif EndPipe == 6: return False
        elif EndPipe == 7: return True

def bfs(i,j):
    q = deque()
    q.append((i,j,MAP[i][j]))
    visited[i][j] = 1
    rs = 1
    time = 1
    while q:
        if time >= L: return rs
        time += 1
        for hour in range(len(q)):
            i,j,pipe = q.popleft()
            for di, dj in movePipe[pipe]:
                ii=i+di
                jj=j+dj
                if 0<=ii<N and 0<=jj<M and visited[ii][jj] == 0:
                    # 간단하게 조건 따지는 법
                    if (-di, -dj) in movePipe[MAP[ii][jj]]:
                    # if canMove(MAP[ii][jj],di,dj):
                        q.append((ii,jj,MAP[ii][jj]))
                        visited[ii][jj] = 1
                        rs+=1
    return rs

for test_case in range(int(input())):
    N,M,i0,j0,L = map(int,input().split())
    MAP = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    sol = bfs(i0,j0)
    print(f'#{test_case+1} {sol}')

