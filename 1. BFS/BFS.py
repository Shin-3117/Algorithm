"""
BFS(Breadth-First Search) 너비 우선 탐색
BFS는 큐 자료구조를 이용

-동작 과정
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 합니다.
2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서
방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리합니다.
3. 더 이상 2번 과정을 수행할 수 없을 때까지 반복
"""

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    #현재 노드 방문 처리
    visited[start]=True
    #큐가 빌 때까지 반복
    while queue:
        #큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v,end=' ')
        #미방문 인접 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True