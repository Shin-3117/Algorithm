import sys
sys.stdin = open("./SW_TEST/IM/1.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N, P = map(int, input().split())
    data=[]
    for i in range(N):
        data.append(list(map(int,input().split())))

    def hit(NUM_row,NUM_col,NUM_P):
        sol = 0
        for i in range(-NUM_P,NUM_P+1):
            if NUM_row+i>=0 and NUM_row+i<N:
                sol += data[NUM_row+i][NUM_col]
            if NUM_col+i>=0 and NUM_col+i<N:
                sol += data[NUM_row][NUM_col+i]
        sol -= data[NUM_row][NUM_col]
        return sol

    max=0

    for row in range(N):
        for col in range(N):
            a= hit(row,col,P)
            if max < a: max=a

    print(f'#{test_case}', max)
"""
#1 75
#2 47
#3 40
#4 81
"""