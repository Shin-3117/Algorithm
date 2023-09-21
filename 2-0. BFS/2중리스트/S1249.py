import sys
sys.stdin = open('./inputs2/S1249.txt','r')

moves = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs():
    # -1이 아니라 float('inf')로 하고 조건을 간략하 하면 더 빠름
    SG = [[-1]*N for _ in range(N)]
    q=[(0,0)]
    SG[0][0]=0
    while q:
        nq = []

        for i,j in q:
            for move in moves:
                ni = i+move[0]
                nj = j+move[1]
                if 0<=ni<N and 0<=nj<N:
                    if SG[ni][nj] == -1:
                        SG[ni][nj] = SG[i][j] + G[ni][nj]
                        if SG[ni][nj] < 0 : SG[ni][nj] = 0
                        nq.append((ni,nj))
                    else:
                        if SG[ni][nj] > SG[i][j] + G[ni][nj]:
                            SG[ni][nj] = SG[i][j] + G[ni][nj]
                            nq.append((ni,nj))
        q = nq
    return SG[N-1][N-1]


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    G = [list(map(int,input().strip())) for _ in range(N)]
    
    # print(G)
    sol = bfs()
    print(f'#{tc} {sol}')