import sys
sys.stdin = open('./inputs/B_2527.txt','r')

for _ in range(4):
    ay0, ax0, ay1, ax1, by0, bx0, by1, bx1 = map(int,input().split())

    if ay1 < by0 or by1 < ay0 or ax1 < bx0 or bx1 < ax0:
        print('d')
        continue
    elif ay0==by1 or by0==ay1:
        if ax1==bx0 or bx1==ax0:
            print('c')
            continue
        else:
            print('b')
            continue
    elif ax1==bx0 or bx1==ax0:
            print('b')
            continue
    else:
        print('a')
        continue

# 메모리 초과 / 메모리 제한 128MB
"""
for _ in range(4):
    ay0, ax0, ay1, ax1, by0, bx0, by1, bx1 = map(int,input().split())
    
    max_y = max(ay1, by1)
    max_x = max(ax1, bx1)
    min_y = min(ay0, by0)
    min_x = min(ax0, bx0)
    # G = [[0]*(max_x+1) for _ in range(max_y+1)]
    G = [[0]*(50001) for _ in range(50001)]
    for y in range(ay0,ay1+1):
        for x in range(ax0,ax1+1):
            G[y][x] += 1
    for y in range(by0,by1+1):
        for x in range(bx0,bx1+1):
            G[y][x] += 1

    clash = []
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            if G[y][x] == 2:
                clash.append((y,x))
    if clash == []:
        print('d')
        continue
    elif len(clash) == 1:
        print('c')
        continue
    # 선분인지 확인
    y_line = clash[0][0]
    isYLine = True
    x_line = clash[0][1]
    isXLine = True
    for lst in clash:
        if lst[0] != y_line:
            isYLine = False
        if lst[1] != x_line:
            isXLine = False
    if isYLine or isXLine:
        print('b')
        continue
    # 남은 경우 면 겹침
    print('a')
"""
