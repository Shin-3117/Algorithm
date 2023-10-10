import sys
sys.stdin = open('./inputs2/S2105.txt','r')

moves = [(1,1),(1,-1),(-1,-1),(-1,1)]
def dfs(i,j,t):
    # 한바퀴 돌아서 도착시, sol 변경
    if t == 4:
        if (i,j) == start:
            global sol
            if sol < sum(C): sol = sum(C)
        return
    # 방문한 적 있는 경우, 동일 디저트일 경우
    if C[G[i][j]] != 0:
        return
    
    ii = i + moves[t-1][0]
    jj = j + moves[t-1][1]
    if 0<ii<N and 0<jj<N:
        if C[G[ii][jj]]==0:
            C[G[i][j]]=1
            print(C)
            dfs(ii,jj,t)
            C[G[i][j]]=0
    else:
        dfs(i,j,t+1)


# 파이썬 15초 50tc
T= int(input())
for tc in range(1):
    N = int(input())
    G = []
    Gmax = 0
    for _ in range(N):
        g = list(map(int, input().split()))
        Gmax = max(Gmax,max(g))
        G.append(g)
    C = [0] * (Gmax+1)
    sol = -1
    for i in range(N):
        for j in range(N):
            # 꼭지점에서 DFS X 어차피 조건 미충족
            if (i,j) == (0,0) or (i,j) == (0,N-1) or (i,j) == (N-1,0) or (i,j) == (N-1,N-1):
                continue
            start = (i,j)
            dfs(i,j,1)

    print(f'#{tc+1} {sol}')