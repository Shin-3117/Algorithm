import sys
sys.stdin = open('./inputs3/B1865.txt','r')
input = sys.stdin.readline

# import heapq
# def dk(start, N, graph):
#     pq=[]
#     heapq.heappush((pq), (0,start))
#     distance = [float('inf')]*(N+1)
#     distance[start] = 0
#     while pq:
#         cost, now = heapq.heappop(pq)
#         if distance[now] < cost: continue

#         for nextList in graph[now]:
#             next = nextList[0]
#             next_cost = nextList[1]
#             total_cost = cost + next_cost
#             if distance[next] > total_cost:
#                 distance[next] = total_cost
#             heapq.heappush(pq, (total_cost, next))
#     return distance

def solution(N, distance, graph):
    distance[1] = 0
    for check in range(N):
        for vertex in range(1, N+1):
            for next_vertex, next_cost in graph[vertex]:
                if distance[next_vertex] > distance[vertex] + next_cost:
                    distance[next_vertex] = distance[vertex] + next_cost
                    if check == N-1:
                        # print(distance)
                        return False
    # print(distance)
    return True

TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    D = [10000]*(N+1)
    G = [[] for _ in range(N+1)]
    for _ in range(M):
        S, E, T = map(int, input().split())
        G[S].append((E,T))
        G[E].append((S,T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        G[S].append((E,-T))
    
    if solution(N, D, G): 
        print("NO")
    else: 
        print("YES")