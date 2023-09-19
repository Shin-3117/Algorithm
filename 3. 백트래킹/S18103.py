import sys
sys.stdin = open('./inputs2/S18103.txt','r')

def bt(position, energy, s):
    global sol
    if position + energy +1 >= goal:
        if sol > s : sol = s
        return
    if s >= sol:
        return
    
    for move in range(energy,0,-1):
        s +=1
        position += move
        bt(position,data[position],s)
        # energy -= data[position]-move
        position -= move
        s -=1


for test_case in range(int(input())):
    data = list(map(int,input().split())) 
    goal = data.pop(0)

    sol = float('inf')

    bt(0,data[0],0)

    print(f'#{test_case+1} {sol}')

# for t in range(int(input())):
#     lst = list(map(int, input().split()))
#     N = lst.pop(0)
#     i = 0
#     cnt = 0
#     while True:
#         if i + lst[i] >= N-1:
#             break
#         cnt += 1
#         max_v = 0
#         # 최대값으로 이동
#         for j in range(i+1, i+1+lst[i]):
#             # index err 방지, max_v는 해당 위치 + charge
#             if j < N-1 and max_v < j - i - 1 + lst[j]:
#                 max_v = j - i - 1 + lst[j]
#                 idx = j
#         i = idx
    
#     print(f'#{t+1}', cnt)