import sys
sys.stdin = open('./SW_TEST/P_A2.txt','r')


dx = [0, 0, -1, 1]  # 상하좌우
dy = [-1, 1, 0, 0]
def catch_zol(move, po):
    if move == 3:
        return
    for d in range(4):
        nx = po[1] + dx[d]
        ny = po[0] + dy[d]

        # 뛰어 넘을 쫄 찾기 # nx,ny는 쫄 위치
        while 0 <= nx < N and 0 <= ny < N and board[ny][nx] == 0:
            nx += dx[d]
            ny += dy[d]
        # 쫄 1개 뛰어넘음
        nx += dx[d]
        ny += dy[d]

        while 0 <= nx < N and 0 <= ny < N:
            if board[ny][nx]:   # 뛰어 넘은 칸에 쫄이 있는 경우
                board[ny][nx] = 0   # catch!
                catch.add((ny, nx))
                catch_zol(move + 1, (ny, nx))   # 잡은 자리에서 다시 탐색 시작
                board[ny][nx] = 1   # 다른 경우의 수 탐색을 위해 복구
                break   # 두 개의 연속으로 붙어있는 쫄을 뛰어 넘는 것은 불가능
            else:   # 뛰어 넘은 칸에 쫄이 없으면 그 자리에서 다시 탐색 시작
                catch_zol(move + 1, (ny, nx))
            # 뛰어 넘을 다른 쫄이 있는지 탐색 시작
            nx += dx[d]
            ny += dy[d]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = []
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(N):
            if row[j] == 2:
                po = (i, j)
                row[j] = 0
        board.append(row)
    catch = set()
    catch_zol(0, po)
    print(f'#{tc} {len(catch)}')