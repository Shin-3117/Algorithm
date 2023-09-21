# 이진 검색(Binary Search) - 반복문

arr = [2, 4, 7, 9, 11, 19, 23]

arr.sort()

def binarySearch(target):
    low = 0
    high = len(arr) - 1
    # 탐색 횟수 카운팅
    cnt = 0

    while low <= high:
        mid = (low + high) // 2
        cnt += 1

        if arr[mid] == target:
            return mid, cnt
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return "해당 데이터는 없습니다", cnt

print(f'9 = {binarySearch(9)}')
print(f'2 = {binarySearch(2)}')
print(f'20 = {binarySearch(20)}')

