"""
입력 받을때 set으로 중복제거

16진수 2진수로 바꾸기

2진수에서 0(101)비율 구하기

비율을 10진수로 편환

변환한 10진수 8개로 쪼개기

8개 단위로 분리한 거 검사(홀수*3+짝수 %10==0)
통과기 결과에 넣기 
"""

# # 0000000000 제거하는 법 : 
# s0='000000'
# s1='000010'
# print(all(char == '0' for char in s0)) # True
# print(all(char == '0' for char in s1)) # False
# print(any(char != '0' for char in s0)) # False
# print(any(char != '0' for char in s1)) # True

#16 진수 2진수로
hex_to_bin = {
    '0':'0000', '1':'0001', '2':'0010', '3':'0011',
    '4':'0100', '5':'0101', '6':'0110', '7':'0111',
    '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
    'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'
}

DICT = {
    "211": 0,
    "221": 1,
    "122": 2,
    "411": 3,
    "132": 4,
    "231": 5,
    "114": 6,
    "312": 7,
    "213": 8,
    "112": 9,
}

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [input().strip() for _ in range(N)]
    # set 구조로 중복 제거
    SET = set(lst)
    result = set()
    newSet = set()
    # 0000000000 제거
    for s in SET:
        if all(c == '0' for c in s) == False:
            newSet.add(s)
    # 16진수 2진수로 변환
    for ns in newSet:
        binaryString = ''
        for char in ns:
            binaryString += hex_to_bin[char]
    # 2진수에서 0(101)비율 구하기
        start = 0
        countArray = []
        for i in range(len(binaryString)):
            if binaryString[i] != binaryString[start]:
                countArray.append(i - start)
                start = i
    # 비율을 10진수로 변환
        pwd = []
        for i in range(1, len(countArray), 4):
            mn = min(countArray[i:i+3])
            key = str(countArray[i]//mn) + str(countArray[i+1]//mn) + str(countArray[i+2]//mn)
            pwd.append(DICT[key])
    # 10진수를 8자리로 분리하고 set에 넣어 중복제거
        for i in range(0, len(pwd), 8):
            result.add(tuple(pwd[i:i+8]))
    # (10진수 8자리)를 검증후 통과시 결과에 더하기
    res = 0
    for r in result:
        if (sum(r[0:8:2]) * 3 + sum(r[1:8:2])) % 10 == 0:
            res += sum(r)

    print(f'#{t} {res}')