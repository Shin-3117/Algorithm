import sys
sys.stdin = open('./inputs3/B1238.txt', 'r')
# 1s
# N: 1000, M: 10000  DFS:11000
from collections import deque
N, M, X = map(int,input().split())
V = [[] for _ in range(N+1)]
Vr = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, time = map(int,input().split())
    V[start].append((end, time))
    Vr[end].append((start,time))

# print(V)
# print(Vr)
def bfs(start,V):
    q=deque()
    visited = [float('inf')]*(N+1)
    visited[start] = 0
    q.append((V[start],0))
    while q:
        
        Vi, t = q.popleft()
        # print(Vi,t)
        for end, time in Vi:
            if visited[end] > time+t:
                visited[end] = time+t
                q.append((V[end], time+t))
                
    return visited

a = bfs(X,V)
b = bfs(X,Vr)
#print(a)
#print(b)
c = [a[i]+b[i] for i in range(1,N+1)]
print(max(c))