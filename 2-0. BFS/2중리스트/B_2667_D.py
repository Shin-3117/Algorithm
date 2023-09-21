# https://www.acmicpc.net/problem/2606
# DFS (44ms, 31332KB)
# BFS (68ms, 34176KB)
# 
import pprint
import sys
from collections import deque
sys.stdin = open('./inputs/B_2667.txt','r', encoding='utf-8')
N = int(sys.stdin.readline())
G =[list(map(int,sys.stdin.readline().strip())) for _ in range(N)]

di,dj=[1,-1,0,0],[0,0,1,-1]
def bfs(i,j):
    rs = 1
    G[i][j] = 0
    q = deque([[i,j]])
    while q:
        i,j = q.popleft()
        for k in range(4):
            ii=i+di[k]
            jj=j+dj[k]
            if 0<=ii<N and 0<=jj<N and G[ii][jj]==1:
                rs+=1
                G[ii][jj]=0
                q.append([ii,jj])
    return rs
sol = []
for i in range(N):
    for j in range(N):
        if G[i][j] == 1:
            sol.append(bfs(i,j))
sol.sort()
print(len(sol))
for i in sol:
    print(i)