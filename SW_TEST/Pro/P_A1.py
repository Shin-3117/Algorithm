import sys
sys.stdin = open('./SW_TEST/P_A1.txt','r')
#6 2 4 8
di = [0,1,0,-1]
dj = [1,0,-1,0]
# 1
directions1 = [2,2,1,2]
curve1 = [2,1,3,3]
# 3
directions3 = [1,0,1,1]
curve3 = [1,3,3,2]
# 7
directions7 = [3,3,3,2]
curve7 = [3,2,1,3]
# 9
directions9 = [3,0,0,0]
curve9 = [3,3,2,1]
for t in range(int(input())):
    N = int(input())
    G = []
    nums = []
    for i in range(N):
        G.append(list(map(int,input().split())))
        for j in range(N):
            if G[i][j] != 0:
                nums.append([G[i][j],i,j])
    nums.sort(reverse=True)
    # print(nums)
    sol = 0
    direction = 0
    position_i = 0
    position_j = 0
    while nums:
        a,i,j = nums.pop()
        # 사과가 키패드 1번 위치에 있을 때
        if position_i < i and position_j > j:
            position_i = i
            position_j = j
            sol += curve1[direction]
            direction = directions1[direction]
        # 사과가 키패드 3번 위치에 있을 때
        if position_i < i and position_j < j:
            position_i = i
            position_j = j
            sol += curve3[direction]
            direction = directions3[direction]
        # 사과가 키패드 7번 위치에 있을 때
        if position_i > i and position_j > j:
            position_i = i
            position_j = j
            sol += curve7[direction]
            direction = directions7[direction]
        # 사과가 키패드 9번 위치에 있을 때
        if position_i > i and position_j < j:
            position_i = i
            position_j = j
            sol += curve9[direction]
            direction = directions9[direction]
    
    print(f'#{t+1} {sol}')