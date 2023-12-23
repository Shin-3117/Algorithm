# 시간 복잡도 BFS(V+N) N=1000^2=1000000 백만 V=4N
# 5백만

import sys
sys.stdin = open('./inputs3/B14940.txt','r')
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
# G = [list(map(int,input().split())) for _ in range(n)]
MAP = []
start = []
for i in range(n):
    g= list(map(int,input().split()))
    if start == []:
        for j in range(m):
            if g[j] == 2:
                start = [i,j]
    MAP.append(g)

# print(n,m)
# print(start)
# print(MAP)
visited = [[-1]*m for _ in range(n)]
# print(visited)
move = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs(start):
    Si,Sj = start
    q = deque()
    q.append((Si,Sj))
    visited[Si][Sj] = 0
    while q:
        i,j = q.popleft()
        for k in move:
            ii = i + k[0]
            jj = j + k[1]
            if 0<=ii<n and 0<=jj<m and visited[ii][jj]==-1:
                if MAP[ii][jj] == 0: 
                    visited[ii][jj] = 0

                elif MAP[ii][jj] == 1:
                    visited[ii][jj] = visited[i][j]+1
                    q.append((ii,jj))

bfs(start)
for i in range(n):
    for j in range(m):
        if MAP[i][j] == 0:
            visited[i][j] = 0
for arr in visited:
    for num in arr:
        print(num, end=' ')
    print()
