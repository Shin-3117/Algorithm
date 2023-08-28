import sys
sys.stdin = open("./SW_TEST/IM/5.txt", "r")

T = int(input())

for t in range(1, T+1):
    N = int( input() )
    data = [list(map(int, input().split())) for _ in range(N+1)]

    sol = 0
    one_positions =[]
    two_position = [0,0]
    for i in range(N+1):
        for j in range(N+1):
            if data[i][j] == 1:
                one_positions.append([i, j])
            if data[i][j] == 2:
                two_position[0] = i
                two_position[1] = j

    cnt = (one_positions[0][0]-two_position[0])**2 + (one_positions[0][1]-two_position[1])**2
    for one_position in one_positions:
        r = (one_position[0]-two_position[0])**2 + (one_position[1]-two_position[1])**2
        if cnt < r:
            cnt = r

    for i in range(1, 16):
        if cnt <= i**2:
            sol = i
            break

    print(f'#{t}', sol)
"""
#1 2
#2 3
#3 3
#4 5
#5 6
"""