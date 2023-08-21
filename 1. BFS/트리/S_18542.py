import sys
sys.stdin = open('./inputs/S_18542.txt','r')
def preorder(idx):
    global num, li
    # i가 노드의 개수를 넘지 않게
    if idx <= N:
        #왼쪽
        preorder(2 * idx)

        li[idx] = num
        num += 1
        #오른쪽
        preorder(2 * idx + 1)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    li = [0] * (N + 1)

    num = 1
    preorder(1)
    print(f'#{tc} {li[1]} {li[N // 2]}')