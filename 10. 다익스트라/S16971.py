# 최소 이동 거리
import sys
sys.stdin = open('./inputs2/S16971.txt','r')

import heapq

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        # 이미 방문한 지점 + 누적 거리가 더 짧게 방문한 적이 있다면 pass
        if distance[now] < dist: continue

        # 인접 노드를 확인
        for next in graph[now]:
            next_node = next[0]
            cost = next[1]
            # next_node 로 가기 위한 누적 거리
            new_cost = dist + cost
            # 누적 거리가 기존보다 크네 면 넘기기
            if distance[next_node] <= new_cost:
                continue

            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))


for tc in range(int(input())):
    # 입력
    n, m = map(int, input().split())
    # 인접리스트
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        f, t, w = map(int, input().split())
        graph[f].append([t, w])

    distance = [float('inf')] * (n+1)
    dijkstra(0)
    sol = distance[-1]

    print(f'#{tc+1} {sol}')