import sys
sys.stdin = open("./SW_TEST/IM/3.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    S, P = map(int, input().split())
    S_lst = list(map(int, input().split()))
    P_lst = list(map(int, input().split()))

    check = -1
    cnt=0
    for p in P_lst:
        for i in range(check+1,S):
            if p == S_lst[i]:
                check = i
                cnt+=1
                break

    sol = 0
    if cnt == P: sol =1
    print(f'#{test_case}', sol)