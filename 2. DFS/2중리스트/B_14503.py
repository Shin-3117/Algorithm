import sys
import pprint
sys.stdin = open('./inputs/B_14503.txt','r', encoding='utf-8')
input = sys.stdin.readline
I,J = map(int,input().split())
i,j,d = map(int,input().split())
G = [list(map(int,input().split())) for _ in range(I)]
di, dj = [-1,0,1,0], [0,1,0,-1]

sol = 0
while True:
    # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if G[i][j] == 0:
        sol +=1
        G[i][j] = 2
    # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    cnt = 0
    for k in range(4):
        ii = i+di[k]
        jj = j+dj[k]
        if G[ii][jj] == 0:
            cnt += 1
    if cnt == 0:
        # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
        ii = i-di[d]
        jj = j-dj[d]
        if G[ii][jj] != 1:
            i = ii
            j = jj
        # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
        else: break
    # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
    elif cnt != 0:
        # 반시계 방향으로 90도 회전한다.
        d = (d+3)%4
        # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
        ii = i+di[d]
        jj = j+dj[d]
        if G[ii][jj] == 0:
            i = ii
            j = jj
print(sol)

