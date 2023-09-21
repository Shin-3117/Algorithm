# 인접 리스트
graph = [
    [1, 3],
    [0, 2, 3, 4],
    [1],
    [0, 1, 4],
    [1, 3],
]


# 큐 bfs
def bfs(start):
    # 노드의 방문 여부를 저장하는 리스트
    visited = [0] * 5

    # 시작 노드를 큐에 추가하고 방문 표시
    queue = [start]
    visited[start] = 1

    while queue:
        # 큐에서 노드를 하나 꺼내고 출력
        now = queue.pop(0)
        print(now, end=' ')

        # 인접한 노드 중에서 방문하지 않은 노드를 큐에 추가하고 방문 표시
        for i in range(len(graph[now])):
            to = graph[now][i]
            if not visited[to]:
                queue.append(to)
                visited[to] = 1


# 0부터 시작하는 BFS를 호출
print("bfs queue = ", end=' ')
bfs(0)
