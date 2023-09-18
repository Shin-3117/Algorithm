# 5204. [파이썬 S/W 문제해결 구현] 4일차 - 병합 정렬
def merge_sort(LST):
    if len(LST) == 1: return LST
    mid = len(LST) // 2
    left = LST[:mid]
    right = LST[mid:]
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    i, j = 0, 0
    global sol
    if left[-1] > right[-1]:
        sol += 1
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # 남은 거 넣기
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

for tc in range(1, 1 + int(input())):
    N = int(input())
    LST = list(map(int, input().split()))
    sol = 0
    sort_LST = merge_sort(LST)

    print(f'#{tc} {sort_LST[N//2]} {sol}')