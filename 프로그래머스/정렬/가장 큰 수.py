def solution(numbers):
    # 1. 모든 수를 문자열로 변환
    numbers = list(map(str, numbers))

    # 2. x+y와 y+x를 비교하여 정렬
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)
    # 3. 정렬된 numbers를 이어붙인 뒤 반환
    answer = ''.join(numbers)

    # 0이 여러개일 경우, "000" 대신 "0"을 반환하도록 예외처리
    if answer[0] == '0':
        return '0'
    else:
        return answer
'''
def solution(numbers):
    answer = ''
    # 4자리로 만들고
    maxs =[]
    for number in numbers:
        if number < 10 :
            N = number*1111
        elif number <100:
            N = number*101
        elif number <1000:
            N = number*1001//100
        maxs.append(N)
    # 4자리로 만든 숫자 오름차순 정렬 (9 8 7)
    sortedList = sorted(maxs, reverse=True)

    # 정렬한 값의 인덱스
    index_list = []
    for i in sortedList:
        index_list.append(maxs.index(i))
    for index in index_list:
        answer += f'{numbers[index]}'
    if answer[0] == '0':
        return '0'
    else:
        return answer


a =solution([0, 0, 0, 0, 9])
print(a)
'''


''' 시간 초과 : 경우의 수 모드 따지는 게 문제인 거 같음
from itertools import permutations

def solution(numbers):
    allLists = list(permutations(numbers, len(numbers)))
#[(6, 10, 2), (6, 2, 10), (10, 6, 2), (10, 2, 6), (2, 6, 10), (2, 10, 6)]
    allLists_len = len(allLists)
    cnt_lst=['' for i in range(allLists_len)]

    # for allList in allLists:
    #     cnt = ''
    #     for num in allList:
    #         cnt +=str(num)
    #     cnt_lst.append(cnt)
    for index in range(allLists_len):
        cnt=''
        for number in allLists[index]:
            cnt +=str(number)
        cnt_lst[index] = cnt

    answer = max(cnt_lst)
    
    return str(int(answer))
'''