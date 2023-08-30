# 4366. 정식이의 은행업무
import sys
sys.stdin = open('./inputs/S_4366.txt','r', encoding='utf-8')

def is23(INT):
    i = 0
    while True:
        a = INT - 2**i


for tc in range(int(input())):
    B = input()
    C = input()
    BL = len(B)
    CL = len(C)
    
    BV = 0
    for i in range(BL):
        BV += int(B[-i-1])*2**i
    # print(BV)
    CV = 0
    for i in range(CL):
        CV += int(C[-i-1])*3**i
    # print(CV)
    minus = abs(BV-CV)
    # print(minus)

    is23(minus)

    print(BV)
    # B_max = 2**(BL)-1
    # C_max = 3**(CL)-1