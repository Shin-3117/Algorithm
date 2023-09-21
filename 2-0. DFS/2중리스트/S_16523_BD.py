import sys
sys.stdin = open('./inputs/S_16523.txt','r', encoding='utf-8')

di,dj = [1,0,-1,0],[0,1,0,-1]

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
    sol = 0
    def dfs(i, j):
        global sol
        C[i][j] = True
        for k in range(4):
            ii = i + di[k]
            jj = j + dj[k]
            if 0<=ii<N and 0<=jj<N and C[ii][jj] == False and G[ii][jj] != 1:
                if G[ii][jj] == 2:
                    sol = 1
                    return
                dfs(ii,jj)
    dfs(pos_i,pos_j)
    print(f'#{t} {sol}')
