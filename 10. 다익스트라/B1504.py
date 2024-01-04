# 다익스트라 
# V^2 = 400 0000 0000
# (V+E)logV = 200800 * 6 1204800
# N = 800, V = 200,000
import sys
sys.stdin = open("./inputs3/B1504.txt","r")
import heapq
input = sys.stdin.readline
n, v = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(v):
    s, e, d = map(int,input().split())
    graph[s].append((e,d))
    graph[e].append((s,d))


def dijkstra(start):
    distance = [float('inf')]*(n+1)
    pq = []
    heapq.heappush(pq, (0,start))
    distance[start] = 0

    while pq:
        sumDistance, nowNode = heapq.heappop(pq)
        if distance[nowNode] < sumDistance: continue

        for next in graph[nowNode]:
            next_node, nextDistance = next
            newDistance = sumDistance + nextDistance
            if distance[next_node] <= newDistance: continue

            distance[next_node] = newDistance
            heapq.heappush(pq,(newDistance, next_node))
    return distance

v1,v2 = map(int,input().split())
oneToList = dijkstra(1)
v1ToList = dijkstra(v1)
v2ToList = dijkstra(v2)

path1 = oneToList[v1]+v1ToList[v2]+v2ToList[n]
path2 = oneToList[v2]+v2ToList[v1]+v1ToList[n]
sol = min(path1,path2)
if sol < float('inf'):
    print(sol)
else: print(-1)