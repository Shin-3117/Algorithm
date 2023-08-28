import sys
sys.stdin = open('./SW_TEST/Pro/P_A3.txt','r')
from itertools import combinations
# from collections import deque
"""
마을의 수 N은 4 이상, 8 이하의 정수이다. 
i번째 마을의 유권자 수 Pi는 1 이상, 20 이하의 정수이다.
마을 r과 마을 c가 인접한 경우, Rrc = 1이며, 
    인접하지 않은 경우 0으로 주어진다. 
Rrc = Rcr을 충족한다.
모든 마을들은 서로 인접하거나 인접한 마을을 통해 연결되어 있다.
모든 마을은 반드시 지역구 중 하나에 포함되어야 한다.

-- idea
1. 지역구를 분리한다.
- 2<N<8 이므로 NC1~N//2 (조합)으로 경우의수를 구하고 최대 : 8+28+56+70
- 각 경우의 수 별로 연결 되어 가능한지 여부를 확인한다.
그래프가 인접행렬방식으로 주어저 연결여부 확인은 O(1)
2. 지역구 값을 더한 값을 차이를 구한다.
"""
# 선택한 마을이 연결되있는 지 확인하는 함수
def isLink(graph,cc):
    L = len(cc)
    E = 0
    for i in range(L):
        for j in range(i,L):
            # 그래프가 인접행렬방식
            if graph[cc[i]][cc[j]] == 1:
                E+=1
    # (간선의 수)가 (노드의 수-1) 보다 많으면 연결된 것
    if L-1 <= E:
        return True
    else: return False

for t in range(int(input())):
    num_villages = int(input())
    G = [list(map(int,input().split())) for _ in range(num_villages)]
    people_in_village = list(map(int,input().split()))
    
    total_people = sum(people_in_village)
    # 무한대
    sol = float('inf')
    
    village_list = list(range(num_villages))
    # 8C1, 8C2, 8C3, 8C4 실행
    for com in range(1,num_villages//2+1):
        group1lst = []
        group2lst = []
        # 조합으로 나온 경우들 그룹1,그룹2에 추가
        for c in combinations(village_list,com):
            group1lst.append(c)
        for c in combinations(village_list,num_villages-com):
            group2lst.append(c)
        # print(group1lst)
        # print(group2lst)
        # 그룹1의 길이 =그룹2의 길이 만큼 반복
        group_num = len(group1lst)
        for idx in range(group_num):
            # 두 개 조합 각각의 마을이 모두 연결되 있는 경우
            if isLink(G,group1lst[idx]) and isLink(G,group2lst[-idx-1]):
                group1_people = 0
                # 마을에 있는 사람 수 더하기
                for village in group1lst[idx]:
                    group1_people += people_in_village[village]
                # A - B -> A - (total-A) -> 2A-total
                abs_group =abs(total_people-2*group1_people)
                # 반복하며 가장 작은 값 저장
                if sol > abs_group:
                    sol = abs_group

    print(f'#{t+1} {sol}')

# g = [
#     [0, 0, 1, 0],
#     [0, 0, 1, 0],
#     [1, 1, 0, 1],
#     [0, 0, 1, 0]
# ]
# l = [(0,), (1,), (2,), (3,)]
# for i in l:
#     if isLink(g,i):
#         print('link')
#     else: print('no')