# SWEA 1219
import sys
sys.stdin = open('./inputs/S_1219.txt','r', encoding='utf-8')
sol = 0
def dfs (Graph, Start):
    global sol
    for i in Graph[Start]:
        if i == 99:
            sol = 1
        elif Graph[i]:
            dfs(Graph, i)
while True:
    try:
        test_case, edge_num = map(int, input().split())
        data = list(map(int, input().split()))

        graph = [[] for _ in range(edge_num)]
        for i in range(edge_num):
            graph[data[i*2]] += [data[i*2+1]]
        
        dfs(graph,0)
        print(f'#{test_case} {sol}')
        
        sol = 0
    except:
        break