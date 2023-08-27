import sys
import pprint
sys.stdin = open('./inputs/B_2116.txt','r')

N = int(input())
dies = []
for _ in range(N):
    A,B,C,D,E,F = map(int,input().split())
    dies.append([A,F,B,D,C,E])

sol = 0
for nun in range(6):
    max_nun = 0

    up = dies[0][nun]
    
    if nun//2 == 0:
        max_nun += max(dies[0][2],dies[0][3],dies[0][4],dies[0][5])
    elif nun//2 == 1:
        max_nun += max(dies[0][0],dies[0][1],dies[0][4],dies[0][5])
    elif nun//2 == 2:
        max_nun += max(dies[0][0],dies[0][1],dies[0][2],dies[0][3])

    for die_num in range(1,N):
        for i in range(6):
            if dies[die_num][i] == up:
                if i%2==0:
                    up = dies[die_num][i+1]
                elif i%2==1:
                    up = dies[die_num][i-1]
                # 01 23 45
                if i//2 == 0:
                    max_nun += max( dies[die_num][2],dies[die_num][3],dies[die_num][4],dies[die_num][5])
                elif i//2 == 1:
                    max_nun += max(dies[die_num][0],dies[die_num][1], dies[die_num][4],dies[die_num][5])
                elif i//2 == 2:
                    max_nun += max(dies[die_num][0],dies[die_num][1],dies[die_num][2],dies[die_num][3] )
                break

    if sol < max_nun: sol = max_nun
print(sol)