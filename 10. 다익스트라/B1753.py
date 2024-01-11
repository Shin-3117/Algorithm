import sys
sys.stdin = open('./inputs3/B1753.txt','r')
import heapq
input =sys.stdin.readline
V, E = map(int, input().split())
startV = int(input())

G = [[] for _ in range(V+1)]
for _ in range(E):
    s,e,w = map(int, input().split())
    G[s].append((e,w))

D = [float('inf')]*(V+1)

def dks(start):
    pq = []
    heapq.heappush(pq,(0,start))
    D[start] = 0

    while pq:
        nowCost, nowNode = heapq.heappop(pq)
        if D[nowNode] < nowCost: continue
        
        for next in G[nowNode]:
            nextNode = next[0]
            nextCost = next[1]
            sumCost = nextCost + nowCost
            if D[nextNode] <= sumCost: continue

            D[nextNode] = sumCost
            heapq.heappush(pq,(sumCost,nextNode))

dks(startV)
for i in range(1,V+1):
    if D[i] == float('inf'): print('INF')
    else: print(D[i])
