# [S/W 문제해결 기본] 9일차 - 중위순회
import sys
sys.stdin = open('./inputs/S_1231.txt','r')
def inorder(v):
    global sol
    # if num_tree[v] == []:
    #     sol += tree[v][1]
    # elif len(num_tree[v]) == 1:
    #     inorder(num_tree[v][0])
    #     sol += tree[v][1]
    # elif len(num_tree[v]) == 2:
    #     inorder(num_tree[v][0])
    #     sol += tree[v][1]
    #     inorder(num_tree[v][1])
    if len(tree[v]) == 2:
        sol += tree[v][1]
    elif len(tree[v]) == 3:
        inorder(tree[v][2])
        sol += tree[v][1]
    elif len(tree[v]) == 4:
        inorder(tree[v][2])
        sol += tree[v][1]
        inorder(tree[v][3])


for tc in range(1, 11):
    N = int(input())
    tree = [[]]
    # num_tree = [[] for _ in range(N+1)]
    for i in range(1,N+1):
        tree.append(list(input().split()))
        for j in range(len(tree[i])):
            if tree[i][j].isdigit():
                tree[i][j] = int(tree[i][j])
    #     L = len(tree[i])
    #     if L == 3:
    #         num_tree[int(tree[i][0])] = [int(tree[i][2])]
    #     elif L == 4:
    #         num_tree[int(tree[i][0])] = [int(tree[i][2]),int(tree[i][3])]
    # print(tree)
    # print(num_tree)
    
    sol=''
    inorder(1)
    print(f'#{tc} {sol}')