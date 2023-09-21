arr = [2, 4, 7, 9, 11, 19, 23]


def binarySearch(low, high, target):
    # 기저조건
    # target 을 발견하지 못하면 종료
    if low > high:
        return -1

    mid = (low + high) // 2

    # 발견했다면
    if target == arr[mid]:
        return mid
    # target 이 mid 보다 작다 == target 이 mid의 왼쪽에 존재한다 == high 를 mid - 1로
    elif target < arr[mid]:
        return binarySearch(low, mid - 1, target)
    else:
        return binarySearch(mid + 1, high, target)


print(f'9 = {binarySearch(0, len(arr) - 1, 9)}')
print(f'2 = {binarySearch(0, len(arr) - 1, 2)}')
print(f'20 = {binarySearch(0, len(arr) - 1, 20)}')

