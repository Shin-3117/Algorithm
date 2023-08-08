"""
DFS(Depth-First Search) :깊이 우선 탐색
DFS는 스택 자료구조 or 재귀 함수를 이용

-동작 과정
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
if 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 
    그 노드를 스택에 넣고 방문 처리
else 스택에서 최상단 노드를 꺼냅니다.
3. 2번 과정을 수행할 수 없을 때까지 반복
"""
#그래프 : 여러 개체들이 연결되어 있는 자료구조
def dfs (graph, v, visited):
    # 핸재 노드v를 방문 처리
    visited[v] = True
    print(v,end=' ')
    
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph_2D=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9#노드가 8이라 9로 지정

dfs(graph_2D,1,visited)