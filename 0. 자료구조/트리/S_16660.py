# 16660. 노드의 합
import sys
sys.stdin = open('./inputs/S_16660.txt','r')

T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int,input().split())
    Tree = [0]*(N+1)
    for _ in range(M):
        a, b = map(int,input().split())
        Tree[a] = b
        while a!=0:
            a = a//2
            Tree[a] += b
    # print(Tree)
    print(f'#{tc} {Tree[L]}')