# https://www.acmicpc.net/problem/14502
"""
1. Idea
-벽만들어야함 (이건 굽했음 다시 풀 땐 없이 하기) # 백트레킹
-벽만들고 BFS로 바이러스 퍼트리기(기존 맵 딥카피 한거)
-남은 0 수 세기
2. O = 5N*M * N*M^3 = (N=8, M=8) 8388만 6080
BFS:O(V+E) = 5N*M
V : N*M
E : 4*V
벽만들기 : N*M

3. data structure
lab_map = int[][]
"""
from collections import deque
import copy
import sys
input = sys.stdin.readline

# 방향 좌표
di = [1,-1,0,0]
dj = [0,0,1,-1]

def bfs():
    q = deque()
    test_map = copy.deepcopy(lab_map)
    # 바이러스(2)위치 찾고 q에 넣기
    for i in range(n):
        for j in range(m):
            if test_map[i][j] == 2:
                q.append([i,j])
    
    # 바이러스(2) 퍼트리기
    while q:
        i,j = q.popleft()
        for k in range(4):
            ii=i+di[k]
            jj=j+dj[k]
            if 0<=ii<n and 0<=jj<m and test_map[ii][jj]==0:
                test_map[ii][jj] = 2
                q.append([ii,jj])
    # 안전 위치의 최댓값 구하기 
    global sol
    cnt = 0
    for i in range(n):
        cnt += test_map[i].count(0)
    if sol < cnt: sol = cnt

    
def make_wall(count):
    if count == 3:
        bfs()
        return
    for i in range(n):
        for k in range(m):
            if lab_map[i][k] == 0:
                lab_map[i][k] = 1
                # 재귀 함수로 벽치는 경우의 수 다 따짐
                make_wall(count+1)
                # 벽세운거 초기화
                lab_map[i][k] = 0

n,m = map(int,input().split())
lab_map = [list(map(int,input().split())) for _ in range(n)]

sol = 0
make_wall(0)

print(sol)