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
def isLink(graph,cc):
    L = len(cc)
    E = 0
    for i in range(L):
        for j in range(i,L):
            if graph[cc[i]][cc[j]] == 1:
                E+=1
    # print(L,E)
    if L-1 <= E:
        return True
    else: return False

for t in range(int(input())):
    num_villages = int(input())
    G = [list(map(int,input().split())) for _ in range(num_villages)]
    people_in_village = list(map(int,input().split()))
    
    total_people = sum(people_in_village)
    sol = float('inf')
    
    village_list = list(range(num_villages))
    for com in range(1,num_villages//2+1):
        group1lst = []
        group2lst = []
        for c in combinations(village_list,com):
            group1lst.append(c)
        for c in combinations(village_list,num_villages-com):
            group2lst.append(c)
        # print(group1lst)
        # print(group2lst)
        group_num = len(group1lst)
        for idx in range(group_num):
            if isLink(G,group1lst[idx]) and isLink(G,group2lst[-idx-1]):
                group1_people = 0
                for village in group1lst[idx]:
                    group1_people += people_in_village[village]
                abs_group =abs(total_people-2*group1_people)
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