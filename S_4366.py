# 4366. 정식이의 은행업무
import sys
sys.stdin = open('./inputs/S_4366.txt','r', encoding='utf-8')


for tc in range(int(input())):
    binary = list(map(int,input().strip()))
    trinary = list(map(int,input().strip()))
    binaryLength = len(binary)
    trinaryLength = len(trinary)
    
    binaryTS10List = []
    for tsIdx in range(binaryLength):
        ts10 = 0
        if binary[tsIdx] == 1:
            binary[tsIdx] = 0
            for i in range(binaryLength):
                ts10 += binary[-i-1]*(2**i)
            binaryTS10List.append(ts10)
            binary[tsIdx] = 1
        elif binary[tsIdx] == 0:
            binary[tsIdx] = 1
            for i in range(binaryLength):
                ts10 += binary[-i-1]*(2**i)
            binaryTS10List.append(ts10)
            binary[tsIdx] = 0

    trinaryTS10List = []
    for tsIdx in range(trinaryLength):
        ts10 = 0
        if trinary[tsIdx] == 0:
            trinary[tsIdx] = 1
            for i in range(trinaryLength):
                ts10 += trinary[-i-1]*(3**i)
            trinaryTS10List.append(ts10)
            ts10 = 0
            trinary[tsIdx] = 2
            for i in range(trinaryLength):
                ts10 += trinary[-i-1]*(3**i)
            trinaryTS10List.append(ts10)
            trinary[tsIdx] = 0
        elif trinary[tsIdx] == 1:
            trinary[tsIdx] = 0
            for i in range(trinaryLength):
                ts10 += trinary[-i-1]*(3**i)
            trinaryTS10List.append(ts10)
            ts10 = 0
            trinary[tsIdx] = 2
            for i in range(trinaryLength):
                ts10 += trinary[-i-1]*(3**i)
            trinaryTS10List.append(ts10)
            trinary[tsIdx] = 1
        elif trinary[tsIdx] == 2:
            trinary[tsIdx] = 0
            for i in range(trinaryLength):
                ts10 += trinary[-i-1]*(3**i)
            trinaryTS10List.append(ts10)
            ts10 = 0
            trinary[tsIdx] = 1
            for i in range(trinaryLength):
                ts10 += trinary[-i-1]*(3**i)
            trinaryTS10List.append(ts10)
            trinary[tsIdx] = 2
    
    # print(binaryTS10List)
    # print(trinaryTS10List)
    sol = 0
    for num in binaryTS10List:
        if num in trinaryTS10List:
            sol = num
            break
    print(f'#{tc+1} {sol}')