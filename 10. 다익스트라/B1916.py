import sys
import heapq
sys.stdin = open('./inputs3/B1916.txt','r')
input = sys.stdin.readline

N = int(input())
M = int(input())
G = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, c = map(int,input().split())
    G[s].append((e,c))
Start, End = map(int,input().split())

# 1. 누적 거리를 계속 저장
distance = [float('inf')] * (N+1)

def dijkstra(start):
    # 2. 우선순위 큐
    pq = []
    # 출발점 초기화
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        # 현재 시점에서
        # 누적 거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(pq)
        # print(dist, now)
        # 이미 방문한 지점 + 누적 거리가 더 짧게 방문한 적이 있다면 pass
        if distance[now] < dist:
            continue

        # 인접 노드를 확인
        for next in G[now]:
            next_node = next[0]
            cost = next[1]

            # next_node 로 가기 위한 누적 거리
            new_cost = dist + cost

            # 누적 거리가 기존보다 크네 면 넘기기
            if distance[next_node] > new_cost:
                distance[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))

dijkstra(Start)
print(distance[End])