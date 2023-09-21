import sys
from collections import deque
sys.stdin = open('./inputs/B_11724.txt','r')
input = sys.stdin.readline

vertex, edge = map(int, input().split())
graph = [[] for _ in range(vertex+1)]
for _ in range(edge):
    a, b = map(int, input().split())
    graph[a]+=[b]
    graph[b]+=[a]

visited = [1]*(vertex+1)

def bfs(Graph,Visited,start):
    Visited[start] = 0
    q =deque()
    q.append(start)
    while q:
        v0 = q.popleft()
        for v1 in Graph[v0]:
            if Visited[v1] == 1:
                Visited[v1] = 0
                q.append(v1)

sol = 0
for i in range(1,vertex+1):
    if visited[i] == 1:
        sol+=1
        bfs(graph,visited,i)
print(sol)