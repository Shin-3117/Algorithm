import sys
sys.stdin = open('./inputs2/S1251.txt','r')

# 모법 답안 252 ms,
# 나 그래프 만들고 prim 돌림
# 그래프 만드는 루프에서 바로 결과 계산 (최소 거리 구해서 lst에 모음)
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    e = float(input())

    di = [float("inf")] * N
    visited = [False] * N

    di[0] = 0
    minsum = 0

    for _ in range(N):
        min_val = float("inf")
        to = -1

        for j in range(N):
            if not visited[j] and di[j] < min_val:
                min_val = di[j] # 0 
                to = j # 0

        visited[to] = True
        minsum += min_val

        for j in range(N):
            if not visited[j]: # 0x 1 2 3 4 5 6...
                temp = (x[to] - x[j]) ** 2 + (y[to] - y[j]) ** 2
                if di[j] > temp:
                    di[j] = temp # 1:temp_min
 
    print(f"#{tc} {round(minsum * e)}")

# """ time 30s
# 섬의 수 : 1≤N≤1,000
# 섬의 좌표 : 0≤X≤1,000,000, 0≤Y≤1,000,000
# 세율 : 0≤E≤1

# prim : O(E log V) = 1000*1001/2*3 = 150_1500
# E=V(V+1)/2
# 그래프를 만들기 N(N+1)/2 = 500500

# O total = 200_2000 + @
# 테스트케이스가 20개이므로 5초 이내 예상
# """
# import pprint
# import heapq
# def prim():
#     MST = [0]*numOfIsland
#     heap = [(0,0)]
#     total_sum = 0

#     while heap:
#         l,v = heapq.heappop(heap)
#         if MST[v]: continue
#         MST[v] = 1
#         total_sum+=l

#         for next in range(numOfIsland):
#             # 갈 수 없거나 이미 방문했다면 pass
#             if graph[v][next] == 0 or MST[next]:
#                 continue
#             heapq.heappush(heap,(graph[v][next],next))
    
#     return total_sum

# T = int(input())
# for testCase in range(1,T+1):
#     numOfIsland = int(input())
#     xOfIslands = list(map(int,input().split()))
#     yOfIslands = list(map(int,input().split()))
#     tax = float(input())

#     graph = [[0]*numOfIsland for _ in range(numOfIsland)]
#     for i in range(numOfIsland): # 0 1 2 3
#         for j in range(i,numOfIsland): #0123 123 23 3
#             LengthSquare = (xOfIslands[i]-xOfIslands[j])**2 + (yOfIslands[i]-yOfIslands[j])**2
#             graph[i][j] = LengthSquare
#             graph[j][i] = LengthSquare
#     # pprint.pprint(graph)
#     sol = round(prim()*tax)
#     print(f'#{testCase} {sol}')

