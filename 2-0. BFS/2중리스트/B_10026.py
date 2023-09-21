import sys
from collections import deque

sys.stdin = open('./inputs/B_10026.txt','r', encoding='utf-8')
input = sys.stdin.readline

N = int(input())
G = [list(input().strip()) for _ in range(N)]
C = [[False]*N for _ in range(N)]
C1 = [[False]*N for _ in range(N)]

di,dj = [1,-1,0,0],[0,0,1,-1]

def bfs(i,j,C,color):
    q=deque()
    q.append([i,j])
    C[i][j] = True
    while q:
        i,j = q.popleft()
        for k in range(4):
            ii=i+di[k]
            jj=j+dj[k]
            if 0<=ii<N and 0<=jj<N:
                if C[ii][jj]==False and G[ii][jj]== color:
                    C[ii][jj]=True
                    
                    q.append([ii,jj])
sol1 = 0
for i in range(N):
    for j in range(N):
        if C[i][j] == False:
            sol1 += 1
            if G[i][j] == 'R':
                bfs(i,j,C,'R')
            elif G[i][j] == 'G':
                bfs(i,j,C,'G')
            elif G[i][j] == 'B':
                bfs(i,j,C,'B')
sol2 = 0
for i in range(N):
    for j in range(N):
        if G[i][j] == 'R':
            G[i][j] = 'G'
for i in range(N):
    for j in range(N):
        if C1[i][j] == False:
            sol2 += 1
            if G[i][j] == 'G':
                bfs(i,j,C1,'G')
            elif G[i][j] == 'B':
                bfs(i,j,C1,'B')

print(sol1, sol2)