T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
 
    # 최대 이익 : max_p
    cnt = 0
    for ls in lst:
        cnt += ls.count(1)
    max_p = M * cnt
 
    # 최대 영역 : max_c
    for c in range(99999):
        cost = c * c + (c - 1) * (c - 1)
        if cost > max_p:
            max_c = c - 1
            break
 
    # 집의 위치 : home
    home = []
    for i in range(N):
        for j in range(N):
            if lst[i][j] == 1:
                home.append((i, j))
 
    # 최대 집 수 : max_h
    max_h = 0
    for k in range(max_c, 0, -1):
        cost_k = k * k + (k - 1) * (k - 1)
        for i in range(N):
            for j in range(N):
                x1, y1 = i, j
                cnt_h = 0
                for h in home:
                    x2, y2 = h
                    if abs(x1 - x2) + abs(y1 - y2) <= k - 1:
                        cnt_h += 1
                if cnt_h * M >= cost_k:
                    if max_h < cnt_h:
                        max_h = cnt_h

        if max_h != 0:
            break

    print(f'#{t} {max_h}')