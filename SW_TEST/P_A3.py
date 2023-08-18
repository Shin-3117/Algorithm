import sys
sys.stdin = open('./SW_TEST/P_A3.txt','r')
"""
마을의 수 N은 4 이상, 8 이하의 정수이다. 
i번째 마을의 유권자 수 Pi는 1 이상, 20 이하의 정수이다.
마을 r과 마을 c가 인접한 경우, Rrc = 1이며, 
    인접하지 않은 경우 0으로 주어진다. 
Rrc = Rcr을 충족한다.
모든 마을들은 서로 인접하거나 인접한 마을을 통해 연결되어 있다.
모든 마을은 반드시 지역구 중 하나에 포함되어야 한다.
"""
for t in range(int(input())):
    N = int(input())
    G = [list(map(int,input().split())) for _ in range(N)]
    Ps = list(map(int,input().split()))

    print(f'#{t+1}')