import sys
sys.stdin = open('./SW_TEST/Pro/P_A6.txt','r')
"""
1. 나무의 개수 N은 2 이상 100 이하로 주어집니다. (2 ≤ N ≤ 100) 
2. 주어지는 나무의 초기 높이는 1 이상 120 이하입니다. 
시간 제한 : 1,000 ms /// 메모리 제한 : 256 MB
---
= idea / O / data structure
나무 정보 받아오고 정렬 trees : int[]
목표 값은 trees[-1]
홀수 날일때는 +1 짝수 날일때는 +2
목표값 - trees[idx] 를 리스트에 저장
리스트의 각 항목 별로 //2 %2 를 각각
2_c, 1_c 에 저장
2_c와 1_c의 값이 같은 경우 답은 2*2_c

1_c가 큰 경우, 2_c만큼 sol+ 
 1_c - 2_c 해서 남은 1_c *2 -1 을 sol+

1_c가 작은 경우,
2_c: -1, 1_c:+2
1_c + 1 >=2_c 까지 반복
1_c만큼 sol+ 
2_c - 1_c 해서 남은 2_c *2 을 sol+
"""
for testCase in range(int(input())):
    sol = 0
    num_tree = int(input())
    trees = list(map(int,input().split()))
    trees.sort()
    target_hight = trees[-1]
    # print(trees)
    c1 = 0
    c2 = 0
    for tree in trees:
        c = target_hight-tree

    print(f'#{testCase+1} {sol}')