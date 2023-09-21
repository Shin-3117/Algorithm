# 3차원 그래프
from collections import deque
import sys
M,N,H = map(int,sys.stdin.readline().split())
sys.stdin = open('./inputs/B_7569.txt','r', encoding='utf-8')
boxes = []
tomatoes = []
for h in range(H):
    cnt = []
    for i in range(N):
        cnt.append(list(map(int, sys.stdin.readline().split())))
        for j in range(M):
            if cnt[i][j] == 1:
                tomatoes.append([h,i,j])
    boxes.append(cnt)

dh = [0,0,0,0,1,-1]
di = [1,-1,0,0,0,0]
dj = [0,0,1,-1,0,0]

q = deque()
q.append(tomatoes)
cnt = -1
while q:
    cnt +=1
    tomato_lst = q.popleft()
    cnt_lst = []
    for tomato in tomato_lst:
        h = tomato[0]
        i = tomato[1]
        j = tomato[2]
        for k in range(6):
            hh = h + dh[k]
            ii = i + di[k]
            jj = j + dj[k]
            if 0<=hh<H and 0<=ii<N and 0<=jj<M:
                if boxes[hh][ii][jj] == 0:
                    boxes[hh][ii][jj] = 1
                    cnt_lst.append([hh,ii,jj])
    if cnt_lst != []:
        q.append(cnt_lst)
sol = cnt
for h in range(H):
    for i in range(N):
        if 0 in boxes[h][i]:
            sol = -1
print(sol)