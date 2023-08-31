import sys
sys.stdin = open('./inputs/S_16918.txt','r')

for t in range(int(input())):
    N = int(input())
    cars = [list(map(int,input().split())) for _ in range(N)]
    cars.sort()

    work_lst = [cars[0]]
    for i in range(1, N):
        # 가장 마지막 작업의 끝나는 시간이
        # 다음 작업의 시작 시간 보다 작다면 추가
        if work_lst[-1][1] <= cars[i][0]:
            work_lst.append(cars[i])
        # 다음 작업의 끝나는 시갑 보다 크다면 변경
        elif work_lst[-1][1] > cars[i][1]:
            work_lst[-1] = cars[i]
    sol = len(work_lst)
    print(f'#{t+1} {sol}')