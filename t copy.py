import sys
sys.stdin = open('./input.txt','r')

def num16to2(datas):
    sol = ''
    for i in datas:
        if i == '0': sol += '0000'
        elif i == '1': sol += '0001'
        elif i == '2': sol += '0010'
        elif i == '3': sol += '0011'
        elif i == '4': sol += '0100'
        elif i == '5': sol += '0101'
        elif i == '6': sol += '0110'
        elif i == '7': sol += '0111'
        elif i == '8': sol += '1000'
        elif i == '9': sol += '1001'
        elif i == 'A': sol += '1010'
        elif i == 'B': sol += '1011'
        elif i == 'C': sol += '1100'
        elif i == 'D': sol += '1101'
        elif i == 'E': sol += '1110'
        elif i == 'F': sol += '1111'
    return sol

def to10(CC):
    C_sol = []
    for C in CC:
        if C == [2,1,1]: C_sol.append(0)
        elif C == [2,2,1]: C_sol.append(1)
        elif C == [1,2,2]: C_sol.append(2)
        elif C == [4,1,1]: C_sol.append(3)
        elif C == [1,3,2]: C_sol.append(4)
        elif C == [2,3,1]: C_sol.append(5)
        elif C == [1,1,4]: C_sol.append(6)
        elif C == [3,1,2]: C_sol.append(7)
        elif C == [2,1,3]: C_sol.append(8)
        elif C == [1,1,2]: C_sol.append(9)
    return C_sol
#[6, 5, 9, 4, 9, 6, 8, 1, 7, 2, 2, 8, 6, 4, 4, 1]

for tc in range(int(input())):
    N,M = map(int,input().split())
    datas = []
    for _ in range(N):
        row_data = input().strip('0')
        if row_data != '':
            if row_data not in datas:
                datas.append(row_data)
    # print(datas)
    # 데이터 숫자로 바꾸기
    
    for data in datas:
        TwoData = num16to2(data)
        # print(TwoData)
        twoData_length = len(TwoData)
        CC = []
        C0101 = [0,0,0]
        cidx = 2
        for reverseIdx in range(twoData_length-1,-1,-1):
            if cidx == 2:
                if TwoData[reverseIdx] == '1':
                    C0101[cidx] +=1
                elif TwoData[reverseIdx] == '0' and C0101[2] != 0:
                    cidx = 1
                    C0101[cidx] +=1
            elif cidx == 1:
                if TwoData[reverseIdx] == '0':
                    C0101[cidx] +=1
                else:
                    cidx = 0
                    C0101[cidx] +=1
            elif cidx == 0:
                if TwoData[reverseIdx] == '1':
                    C0101[cidx] +=1
                else:
                    div = min(C0101)
                    C0101 = list(map(lambda x: x//div,C0101))
                    CC.append(C0101)
                    C0101 = [0,0,0]
                    cidx = 2
        # print(CC)
        nums = to10(CC)
        # 뒤집기
        nums = nums[::-1]
        # print(nums)
        
        L = len(nums)//8
        for l in range(L):
            cnt = 0
            for i in range(l*8,l*8+8):
                if i%2==0:
                    cnt+=nums[i]*3
                else: cnt+=nums[i]
            if cnt %10 ==0:
                sol_cnt = 0
                for i in range(l*8,l*8+8):
                    sol_cnt +=nums[i]
    sol = sol_cnt
    print(f'#{tc + 1} {sol}')

