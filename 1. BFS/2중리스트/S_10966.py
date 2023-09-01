# 10966. 물놀이를 가자
import sys
sys.stdin = open('./inputs2/S_10966.txt','r')
"""
제한 시간 6초
1 <= I,J <= 10^3
BFS : O(V+E) : E=4V V=(10^3)^2 = 10^6 => O = 5*10^6
for문 : (10^3)^2
test case = 20
total = 20*6*10^6 = 1,2000,0000 => time in
W에서 시작하기
"""
from collections import deque
# direction_i = [1,-1,0,0]
# direction_j = [0,0,1,-1]
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def bfs(Q):
    while Q:
        i,j = Q.popleft()
        # for move in range(4):
        #     ii = i+direction_i[move]
        #     jj = j+direction_j[move]
        for dx, dy in direction:
            ii, jj = i + dx, j + dy
            if 0<=ii<I and 0<=jj<J and visited[ii][jj]==-1 and MAP[ii][jj] == 'L':
                visited[ii][jj] = visited[i][j] + 1
                Q.append((ii,jj))


for test_case in range(int(input())):
    I, J = map(int,input().split())
    MAP = []
    # None에서 숫자로 바꾸는 거보다 -1 에서 0으로 변경이 빠름
    visited = [[-1]*J for _ in range(I)]
    Waters = deque()
    for i in range(I):
        MAP.append(input())
        for j in range(J):
            if MAP[i][j] == 'W':
                Waters.append([i,j])
                visited[i][j] = 0
    
    bfs(Waters)
    sol = 0
    for i in range(I):
        sol += sum(visited[i])
    # print(visited)
    print(f'#{test_case+1} {sol}')