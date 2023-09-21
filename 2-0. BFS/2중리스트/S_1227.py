# 미로 2
import sys
sys.stdin = open('./inputs/S_1227.txt','r')

from collections import deque
di,dj = [1,-1,0,0],[0,0,1,-1]
def bfs(i,j):
    # q=[[i,j]]
    q=deque()
    q.append([i,j])
    C[i][j] =True
    while q:
        # i,j = q.pop(0)
        i,j = q.popleft()
        for k in range(4):
            ii = i +di[k]
            jj = j +dj[k]
            if ii == start_i and jj == start_j:
                return 1
            if 0<=ii<100 and 0<=jj<100:
                if C[ii][jj] == False and G[ii][jj] == '0':
                    C[ii][jj] = True
                    q.append([ii,jj])
    return 0

for t in range(1,11):
    input()
    G = []
    for i in range(100):
        G.append(input())
        for j in range(100):
            if G[i][j] == '3':
                end_i = i
                end_j = j
            elif G[i][j] == '2':
                start_i = i
                start_j = j
    C = [[False]*100 for _ in range(100)]

    sol = bfs(end_i,end_j)
    print(f'#{t} {sol}')