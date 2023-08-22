import sys
sys.stdin = open('./SW_TEST/P_A5.txt','r')

input = sys.stdin.readline
# 방향 백터
dr = [
        [-1,-1,-1,0,0,1],
        [-1,0,0,1,1,1]
    ]
dc = [
    [0,-1,1,-1,1,0],
    [0,-1,1,-1,1,0]
]

def dfs(row, col, level, sum):
        global ans, visited
        if level >= 4:
            ans = max(ans, sum)
            return
        for i in range(6):
            nr = row + dr[col % 2][i]
            nc = col + dc[col % 2][i]
            # if nr < 0 or nr >= N or nc < 0 or nc >= M :
            #     continue
            # if visited[nr][nc] != 0 :
            #     continue
            if 0<=nr<N and 0<=nc<M and visited[nr][nc]==0:
                visited[nr][nc] = 1
                dfs(nr, nc, level + 1, sum + MAP[nr][nc])
                visited[nr][nc] = 0

def etc(row, col):
    com = [
        [0,3,4],
        [1,2,5]
    ]
    ret = -1
    for i in range(2):
        sum = MAP[row][col]
        for j in range(3):
            nr = row + dr[col % 2][com[i][j]]
            nc = col + dc[col % 2][com[i][j]]
            if nr < 0 or nr >= N or nc < 0 or nc >= M :
                sum = -1
                break
            sum += MAP[nr][nc]
        ret = max(sum, ret)
    return ret

for tc in range(int(input())):
    # 초기 입력 값 & visited
    N, M = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    
    ans = 0
    
    for i in range(N):
        for j in range(M):
            visited[i][j] = 1
            dfs(i, j, 1, MAP[i][j])
            visited[i][j] = 0
            ans = max(ans, etc(i, j))
    print(f'#{tc+1}',ans)