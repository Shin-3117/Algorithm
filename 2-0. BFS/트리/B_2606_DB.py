# https://www.acmicpc.net/problem/2606
import sys
from collections import deque
sys.stdin = open('./inputs/B_2606.txt','r')
input = sys.stdin.readline

vertex = int(input())
edge = int(input())
graph = [[] for _ in range(vertex+1)]
for i in range(edge):
    a,b=map(int,input().split())
    graph[a]+=[b]
    graph[b]+=[a]
visited = [0]*(vertex+1)

def bfs(gragh, visited, start):
    visited[start] = 1
    q = deque()
    q.append(start)
    while q:
        current_vertex = q.popleft()
        for next_vertex in gragh[current_vertex]:
            if visited[next_vertex] == 0:
                visited[next_vertex] = 1
                q.append(next_vertex)

bfs(graph,visited,1)
print(sum(visited)-1)
