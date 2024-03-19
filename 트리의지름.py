#B1967
#트리의 지름 :트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이를 말한다.
#  n(1 ≤ n ≤ 10,000), 제한시간 2초
# BFS 1번 돌려서 가장 거리가 먼 지점에서 다시 BFS
# BFS = O(V+E) 20,000 BFS 두번 20,000 + 20,000 타임인

from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
# print(graph)
for i in range(n-1):
    s,e,d = map(int,input().split())
    graph[s].append([e,d])
    graph[e].append([s,d])

q=deque()
q.append([1,0])
visited = [0]*(n+1)
distance = [0]*(n+1)
while q:
    v, d = q.popleft()
    visited[v] = 1
    for vv,dd in graph[v]:
        if visited[vv] == 0:
            distance[vv]=d+dd
            q.append([vv,d+dd])

maxNode = 0
maxDistance = 0
for idx, item in enumerate(distance):
    if item > maxDistance: 
        maxDistance = item
        maxNode = idx

q=deque()
q.append([maxNode,0])
visited = [0]*(n+1)
distance = [0]*(n+1)
while q:
    v, d = q.popleft()
    visited[v] = 1
    for vv,dd in graph[v]:
        if visited[vv] == 0:
            distance[vv]=d+dd
            q.append([vv,d+dd])

print(max(distance))