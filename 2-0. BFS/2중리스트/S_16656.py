# 미로의 거리
import sys
sys.stdin = open('./inputs/S_16656.txt','r')
import pprint
di = [1,-1,0,0]
dj = [0,0,1,-1]

def bfs(i,j):
    q = []
    q.append([i,j])
    # G[i][j] = 1
    while q:
        i,j = q.pop(0)
        for k in range(4):
            ii = i + di[k]
            jj = j + dj[k]
            if ii == start_i and jj == start_j:
                return G[i][j]
            if 0<=ii<N and 0<=jj<N:
                if G[ii][jj] == 0:
                    G[ii][jj] = G[i][j] + 1
                    q.append([ii,jj])
    return 3

for t in range(int(input())):
    N = int(input())
    G = []
    for i in range(N):
        G.append(list(map(int,input().strip())))
        for j in range(N):
            if G[i][j] == 3:
                end_i = i
                end_j = j
            elif G[i][j] ==2:
                start_i = i
                start_j = j
    print(end_i,end_j)
    sol = bfs(end_i,end_j)
    pprint.pprint(G)
    print(f"#{t+1} {sol-3}")