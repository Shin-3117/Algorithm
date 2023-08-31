# 1861. 정사각형 방
import sys
sys.stdin = open('./inputs/S_1861.txt','r')
"""
제한시간 4초
bfs로 풀시 시간복잡도 (가능)
O(V+E) = 5*N**2 = 5*(10**3)**2 = 500,0000
 V : N**2
 E : 4V
 N (1 ≤ N ≤ 10**3)
"""
# 방향 백터
di = [1,-1,0,0]
dj = [0,0,1,-1]
 
def bfs(i0,j0):
    global start_point, total_moves
    # visited[i][j] = 1
    q = [(i0,j0)]
    moves = 1
    while q:
        i,j = q.pop(0)
        for move in range(4):
            ii = i+di[move]
            jj = j+dj[move]
            # MAP 밖으로 나가지 않았으면
            if 0<=ii<N and 0<=jj<N:
                #이동하려는 방이 현재 방보다 1크다면 
                if MAP[i][j]+1 == MAP[ii][jj]:
                    q.append((ii,jj))
                    moves += 1
    if moves > total_moves:
        total_moves = moves
        start_point = MAP[i0][j0]
    elif moves == total_moves:
        if start_point > MAP[i0][j0]:
            start_point = MAP[i0][j0]
 
total_test_case = int(input())
for test_case in range(total_test_case):
    N = int(input())
    MAP = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
 
    start_point = float('inf')
    total_moves = 0
    for i in range(N):
        for j in range(N):
            bfs(i,j)
 
    print(f'#{test_case+1} {start_point} {total_moves}')
