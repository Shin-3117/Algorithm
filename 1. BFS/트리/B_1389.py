"""
제한시간 2초
BFS
O(V+E) : V=100 E=5000 => 5100
for문 V만큼
51,0000
"""
import sys
from collections import deque
sys.stdin = open('./inputs2/B_1389.txt','r')
# 유저의 수 N (2 ≤ N ≤ 100), 친구 관계의 수 M (1 ≤ M ≤ 5,000)
N, M = map(int,input().split())
N_lst = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int,input().split())
    N_lst[a].append(b)
    N_lst[b].append(a)
# print(N_lst)
sol = 0
KevinBaconNum = float('inf')
for i in range(1,N+1):
    q = deque()
    q.append(i)
    visited = [-1 for _ in range(N+1)]
    # print(visited)
    cnt = 0
    visited[i] = cnt
    
    while q:
        cnt += 1
        for _ in range(len(q)):
            vn = q.popleft()
            for v in N_lst[vn]:
                if visited[v] == -1:
                    q.append(v)
                    visited[v] = cnt
    # print(sum(visited)+1)
    if KevinBaconNum > sum(visited)+1:
        KevinBaconNum = sum(visited)+1
        sol = i
print(sol)