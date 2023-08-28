import sys
sys.stdin = open("./SW_TEST/IM/2.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    data = []
    for i in range(N):
        data.append(list(map(int, input().split())))

    sol = 0

    max = 0
    cnt = 0
    def findSquare(ROW, COL):
        global max
        global cnt
        for r in range(ROW, N):
            for c in range(COL, N):
                if data[ROW][COL] == data[r][c]:
                    big_square_size = (1+r-ROW)*(1+c-COL)
                    if max < big_square_size:
                        max = big_square_size
                        cnt = 1
                    elif max == big_square_size:
                        cnt += 1
        return cnt

    for row in range(N):
        for col in range(N):
            a = findSquare(row, col)
    sol = a

    print(f'#{test_case}', sol)