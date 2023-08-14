from collections import deque
import sys
sys.stdin = open('./inputs/S_16523.txt','r', encoding='utf-8')
di,dj = [1,0,-1,0],[0,1,0,-1]

def bfs(i, j, G, C):
    q = deque()
    q.append([i, j])
    C[i][j] = True
    while q:
        i, j = q.popleft()
        for k in range(4):
            ii = i + di[k]
            jj = j + dj[k]
            if 0 <= ii < N and 0 <= jj < N and C[ii][jj] == False and G[ii][jj] != 1:
                if G[ii][jj] == 2:
                    return 1
                C[ii][jj] = True
                q.append([ii, jj])
    return 0

for t in range(1,int(input())+1):
    N = int(input())
    G = []
    for i in range(N):
        G.append(list(map(int, input().strip())))
        for j in range(N):
            if G[i][j] == 3:
                pos_i = i
                pos_j = j

    C = [[False]*N for _ in range(N)]

    sol = bfs(pos_i,pos_j,G,C)
    print(f'#{t} {sol}')
