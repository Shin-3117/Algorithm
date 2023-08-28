import sys
sys.stdin = open("./SW_TEST/IM/4.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    R, C = map(int, input().split())
    Answer = list(map(int,input().split()))
    data = [list(map(int,input().split())) for _ in range(R)]

    cnt = 0
    total = 0
    total_lst = []
    for j in range(R):
        cnt = 0
        total = 0
        for i in range(C):
            if Answer[i] == data[j][i]:
                cnt += 1
                total += cnt
            else:
                cnt = 0
        total_lst.append(total)
    print(f'#{test_case}', max(total_lst)-min(total_lst))