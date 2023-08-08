# https://www.acmicpc.net/problem/7576
"""
1. idea
이중 for문으로 1의 위치 찾고
BFS
BFS에서 시간 계산 해서 반환
2. O BFS:O(V+E) = 5N*M
V : N*M
E : 4*V

3. 자료구조
data : int[][]
cc : boolean[][]
sol : int
"""
import pprint
import sys
from collections import deque
J,I = map(int,sys.stdin.readline().split())
data = [list(map(int,sys.stdin.readline().split())) for _ in range(I)]
cc = [[False]*J for _ in range(I)]
di,dj=[1,-1,0,0],[0,0,1,-1]
# 동시처리는 일단 나누기 2 해보는 걸로
def bfs(LIST):
    q = deque()
    for i in LIST:
        q.append(i)
    rs =0
    while q:
        i,j=q.popleft()
        for k in range(4):
            ii=i+di[k]
            jj=j+dj[k]
            if 0<=ii<I and 0<=jj<J :#and cc[ii][jj]==False
                if data[ii][jj] == 0:
                    data[ii][jj] = data[i][j]+1
                    cc[ii][jj]=True
                    q.append([ii,jj])
                    rs=data[ii][jj]
    return rs
sol = 0
cnt = []
for i in range(I):
    for j in range(J):
        if data[i][j] == 1:
            cc[i][j] = True
            cnt.append([i,j])
bfs(cnt)
# pprint.pprint(data)
for i in data:
    if max(i)-1 > sol: sol = max(i)-1
for i in range(I):
    for j in range(J):
        if data[i][j] == 0:
            sol = -1
print(sol)