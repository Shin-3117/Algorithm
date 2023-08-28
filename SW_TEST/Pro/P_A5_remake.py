import sys
sys.stdin = open('./SW_TEST/P_A5.txt','r')
# 벌집 4개 썰어서(이어지게) 가장 큰 값 찾기
input = sys.stdin.readline
#j가 홀수 일때 이동가능 경로 시계방향
di1 = [-1,0,1,1,1,0]
dj1 = [0,1,1,0,-1,-1]
#j가 짝수 일때 이동가능 경로 시계방향
di0 = [-1,-1,0,1,0,-1]
dj0 = [0,1,1,0,-1,-1]

def dfs(i,j,rs,m):
    global sol, C
    if m >= 4:
        sol = max(sol,rs)
        return

    for k in range(6):
        if j%2 ==0:
            ii = i + di0[k]
            jj = j + dj0[k]
        else:
            ii = i + di1[k]
            jj = j + dj1[k]

        if 0<=ii<I and 0<=jj<J and C[ii][jj] == False:
            C[ii][jj] = True
            dfs(ii,jj,rs+G[ii][jj],m+1)
            C[ii][jj] = False
#dfs로 조회가 불가능한 삼각형 모양
def etc(row, col):
    com = [
        [0,4,2],
        [5,1,3]
    ]
    ret = -1
    for i in range(2):
        sum = G[row][col]
        for j in range(3):
            if col%2 ==0:
                nr = row + di0[com[i][j]]
                nc = col + dj0[com[i][j]]
            else:
                nr = row + di1[com[i][j]]
                nc = col + dj1[com[i][j]]
            # nr = row + dr[col % 2][com[i][j]]
            # nc = col + dc[col % 2][com[i][j]]
            if nr < 0 or nr >= I or nc < 0 or nc >= J :
                sum = 0
                break
            sum += G[nr][nc]
        ret = max(sum, ret)
    return ret

for t in range(int(input())):
    I,J = map(int,input().split())
    G = [list(map(int,input().split())) for _ in range(I)]
    C = [[False]*J for _ in range(I)]

    sol = 0
    
    for i in range(I):
        for j in range(J):
            C[i][j] = True
            dfs(i,j,G[i][j],1)
            C[i][j] = False
            sol = max(sol,etc(i,j))
    print(f'#{t+1} {sol}')
