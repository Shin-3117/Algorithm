# 1 ≤ X ≤ N ≤ 1,000, 1 ≤ M ≤ 10,000
import heapq
def dijkstra(start,G):
    distance = [float('inf')]*(Vn+1)
    pq=[]
    heapq.heappush(pq,(0,start))
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] < dist: continue

        for next in G[now]:
            nextNode = next[0]
            nextDist = next[1]

            nowDist = nextDist + dist

            if distance[nextNode] <= nowDist: continue

            distance[nextNode] = nowDist
            heapq.heappush(pq,(nowDist,nextNode))
    return distance

T = int(input())
for tc in range(T):
    Vn, En, goal = map(int,input().split())
    V = [[] for _ in range(Vn+1)]
    RV = [[] for _ in range(Vn+1)]
    for _ in range(En):
        startNode, endNode, dist = map(int,input().split())
        V[startNode].append((endNode,dist))
        RV[endNode].append((startNode,dist))
    # RV로 획기적으로 시간 줄임 ㄷㄷ 2365->388
    goalToStart = dijkstra(goal,V)
    startToGoal = dijkstra(goal,RV)
    sol = 0
    for i in range(1,Vn+1):
        sol = max(sol,goalToStart[i]+startToGoal[i] )
    print(f'#{tc+1} {sol}')