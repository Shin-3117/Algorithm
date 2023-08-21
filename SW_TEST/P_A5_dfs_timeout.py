import sys
sys.stdin = open('./SW_TEST/P_A5.txt','r')
"""
1초
3 <= N, M <= 15
포문 15*15
dfs O(V+E) : V+6V = 7*15*15
7*15*15*15*15 = 354375
"""
input = sys.stdin.readline
#j가 홀수 일때 이동가능 경로
di1 = [-1,0,0,1,1,1]
dj1 = [0,-1,1,-1,0,1]
#j가 짝수 일때 이동가능 경로
di0 = [-1,-1,-1,0,0,1]
dj0 = [-1,0,1,-1,1,0]

def dfs(i,j,rs,m):
    global sol
    if m == 5:
        sol = max(sol,rs)
        return
    rs += G[i][j]
    # 방문처리
    C[i][j] = True
    # C.append([i,j])
    # 0 2 4 위치
    if j%2 ==0:
        for k in range(6):
            ii = i + di0[k]
            jj = j + dj0[k]
            if 0<=ii<I and 0<=jj<J:
                if C[ii][jj] == False:
                # if not [ii,jj] in C:
                    dfs(ii,jj,rs,m+1)
    else:
        for k in range(6):
            ii = i + di1[k]
            jj = j + dj1[k]
            if 0<=ii<I and 0<=jj<J:
                if C[ii][jj] == False:
                # if not [ii,jj] in C:
                    dfs(ii,jj,rs,m+1)
    # rs -= G[i][j]
    C[i][j] = False
    # C.pop()
T = int(input())
for t in range(T):
    I,J = map(int,input().split())
    G = [list(map(int,input().split())) for _ in range(I)]
    C = [[False]*J for _ in range(I)]
    # C=[]
    sol = 0
    
    for i in range(I):
        cnt = 0
        for j in range(J):
            
            dfs(i,j,0,1)
            # C[i][j] = True
            # C.append([i,j])
            if 1<=i<I-1 and 1<=j<J-1:
                if j%2 ==0:
                    upY = G[i][j]+G[i-1][j-1]+G[i-1][j+1]+G[i+1][j]
                    downY = G[i][j]+G[i-1][j]+G[i][j+1]+G[i][j-1]
                else:
                    upY = G[i][j]+G[i][j-1]+G[i][j+1]+G[i+1][j]
                    downY = G[i][j]+G[i-1][j]+G[i+1][j+1]+G[i+1][j-1]
                sol = max(sol,upY,downY)
            elif i == 0 and 1<=j<J-1 and j%2==1:
                upY = G[i][j]+G[i][j-1]+G[i][j+1]+G[i+1][j]
                sol = max(sol,upY)
            elif i == I-1 and 1<=j<J-1 and j%2==0:
                downY = G[i][j]+G[i-1][j]+G[i][j+1]+G[i][j-1]
                sol = max(sol,downY)
    print(f'#{t+1} {sol}')
