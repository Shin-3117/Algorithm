# https://www.acmicpc.net/problem/2178
"""
1. Idea
시작은 0,0 고정
도착은 N,M
BFS로 값을 받고
가장 작은 값을 정답으로 제출

2. 시간 복잡도 BFS:O(V+E) = 5 N*M
V : N*M
E : V*4

3. 자료구조
data : int[][]
chk : boolean[][]
sol : int[]
"""
import sys
from collections import deque
sys.stdin = open('./inputs/B_2178.txt','r', encoding='utf-8')
N,M = map(int,sys.stdin.readline().split())
data = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)]

di,dj =[-1,1,0,0], [0,0,-1,1]

def bfs(i,j):
    q = deque()
    q.append((i,j))
    while q:
        ei, ej = q.popleft()
        for k in range(4):
            ni = ei+di[k]
            nj = ej+dj[k]
            if 0<=ni<N and 0<=nj<M and data[ni][nj] == 1:
                    q.append([ni,nj])
                    data[ni][nj] = data[ei][ej] + 1
    return data[N-1][M-1]

print(bfs(0,0))