import sys
sys.stdin = open('./SW_TEST/P_A5.txt','r')

#j가 홀수 일때 이동가능 경로
di1 = [-1,0,0,1,1,1]
dj1 = [0,-1,1,-1,0,1]
#j가 짝수 일때 이동가능 경로
di2 = [-1,-1,-1,0,0,1]
dj2 = [-1,0,1,-1,1,0]
# 삼각형 체크를 못함
def dfs(move,i,j,cnt):
    global sol
    if move == 4: 
        if cnt > sol:
            sol = cnt
        return
    C[i][j] = True
    if j%2 == 1:
        for k in range(6):
            ii = i + di1[k]
            jj = j + dj1[k]
            if 0<=ii<I and 0<=jj<J and C[ii][jj] == False:
                cnt += G[ii][jj]
                C[ii][jj] = True
                dfs(move+1,ii,jj,cnt)
                cnt -= G[ii][jj]
                C[ii][jj] = False
    elif j%2 == 0:
        for k in range(6):
            ii = i + di2[k]
            jj = j + dj2[k]
            if 0<=ii<I and 0<=jj<J and C[ii][jj] == False:
                cnt += G[ii][jj]
                C[ii][jj] = True
                dfs(move+1,ii,jj,cnt)
                cnt -= G[ii][jj]
                C[ii][jj] = False

for t in range(int(input())):
    I,J = map(int,input().split())
    G = [list(map(int,input().split())) for _ in range(I)]
    C = [[False]*J for _ in range(I)]
    sol = 0
    cnt = 0
    for i in range(I):
        for j in range(J):
            dfs(0,i,j,0)
            if 1<=i<I-1 and 1<=j<J-1:
                if j%2 ==0:
                    upY = G[i][j]+G[i-1][j-1]+G[i-1][j+1]+G[i+1][j]
                    downY = G[i][j]+G[i-1][j]+G[i][j+1]+G[i][j-1]
                    sol = max(sol,upY,downY)
                else:
                    upY = G[i][j]+G[i][j-1]+G[i][j+1]+G[i+1][j]
                    downY = G[i][j]+G[i-1][j]+G[i+1][j+1]+G[i+1][j-1]
                    sol = max(sol,upY,downY)
            elif i==0 and 0<=j<J-2:
                # p =
                # b =
                pass
    
    print(f'#{t+1} {sol}')