# [S/W 문제해결 기본] 9일차 - 사칙연산
import sys
sys.stdin = open('./inputs/S_1232.txt','r')

def dfs(s):
    while not isinstance(Tree_data[s], int):
        LeftNode = Tree_data[Tree_address[s][0]]
        RightNode = Tree_data[Tree_address[s][1]]
        #자식 노드가 숫자가 아닌 경우, 자식노드로 이동
        if not isinstance(LeftNode, int):
            dfs(Tree_address[s][0])
        if not isinstance(RightNode, int):
            dfs(Tree_address[s][1])
        # 좌우 자식노드가 숫자인 경우
        if isinstance(LeftNode, int) and isinstance(RightNode, int):
            rs = 0
            # 사칙연산
            if Tree_data[s] == '+':
                rs = LeftNode + RightNode
            elif Tree_data[s] == '-':
                rs = LeftNode - RightNode
            elif Tree_data[s] == '*':
                rs = LeftNode * RightNode
            elif Tree_data[s] == '/':
                rs = LeftNode // RightNode
            # 사칙연산 결과값을 노드에 바꿔주기 : 기호->숫자
            Tree_data[s] = rs


for t in range(10):
    N = int(input())
    Tree_data = [0 for _ in range(N+1)]
    Tree_address = [[] for _ in range(N+1)]
    for _ in range(N):
        data = list(input().split())
        if len(data) == 4:
            Tree_address[int(data[0])] = [int(data[2]),int(data[3])]

        if data[1].isdigit():
            Tree_data[int(data[0])] = int(data[1])
        else: Tree_data[int(data[0])] = data[1]

    dfs(1)
    sol = Tree_data[1]

    print(f'#{t+1} {sol}')
