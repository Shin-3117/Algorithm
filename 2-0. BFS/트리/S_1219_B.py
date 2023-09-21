# SWEA 1219
import sys
sys.stdin = open('./inputs/S_1219.txt','r', encoding='utf-8')

from collections import deque
def bfs (Graph, Start):
    q = deque()
    q.append(Start)
    while q:
        v = q.popleft()
        for i in Graph[v]:
            if i == 99:
                return 1
            elif Graph[i]:
                q.append(i)
    return 0        
# 테스트 케이스를 모름으로 입력 받을 값이 없을 경우(error) break
while True:
    try:
        test_case, edge_num = map(int, input().split())
        data = list(map(int, input().split()))
        
        # 그래프 초기 세팅
        graph = [[] for _ in range(edge_num)]
        for i in range(edge_num):
            graph[data[i*2]] += [data[i*2+1]]
        # [[1, 2], [4, 3], [9, 5], [7], [8, 3], [6, 7], [10], [99, 9], [], [8, 10], [], [], [], [], [], []]
        
        sol = bfs(graph,0)
        print(f'#{test_case} {sol}')

    except:
        break